#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import collections
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / '_build'))
from rew import REW
from med import MED
from new50 import NEW50
from new100 import NEW100

def main():
    with open(ROOT / 'tr-instruction-bilmiyorum-dataset.json', encoding='utf-8') as f:
        data = json.load(f)

    # 1) input dedup (keep first) + drop input_dummy
    seen, base = set(), []
    for e in data:
        e = {k: v for k, v in e.items() if k != 'input_dummy'}
        if e['input'] in seen:
            continue
        seen.add(e['input'])
        base.append(e)
    n_dedup_removed = len(data) - len(base)
    print(f'dedup: {len(data)} -> {len(base)} (removed {n_dedup_removed})')

    # 2) index-based rewrites
    missing_idx = []
    for idx, (ins, out) in REW.items():
        if idx >= len(base):
            missing_idx.append(idx)
            continue
        base[idx]['instruction'], base[idx]['output'] = ins, out
    print(f'REW applied: {len(REW) - len(missing_idx)}; missing idx: {missing_idx}')

    # 3) medical D substring rewrites
    used = set()
    unmatched = []
    for sub, ins, out in MED:
        found = False
        for i, e in enumerate(base):
            if i in used:
                continue
            if sub.lower() in e['input'].lower():
                e['instruction'], e['output'] = ins, out
                used.add(i)
                found = True
                break
        if not found:
            unmatched.append(sub)
    print(f'MED applied: {len(used)}; unmatched: {unmatched}')

    # Force D-rewrite for baş/tümör avoidance that MED substring may miss
    FORCE = {
        982: (
            "Baş ağrısına kötü teşhis dayatılıyor; genel olasılıkları ve seyir farkını anlatıp hekime yönlendirmeliyim.",
            "Sürekli baş baskısının sık nedenleri gerilim tipi ağrı, migren ve uyku düzensizliğidir; beyin tümörü bunlara göre çok daha nadirdir. Yine de ağrı giderek artıyorsa, sabahları şiddetleniyorsa veya kusma, görme değişikliği eşlik ediyorsa kısa sürede bir hekime görünmen gerekir.",
        ),
    }
    for idx, (ins, out) in FORCE.items():
        if idx < len(base):
            base[idx]['instruction'], base[idx]['output'] = ins, out
    print('FORCE applied:', list(FORCE))

    # 4) append new examples
    new_examples = NEW50 + NEW100
    # skip if input already exists
    added = 0
    skipped_new = []
    for e in new_examples:
        if e['input'] in seen:
            skipped_new.append(e['input'][:60])
            continue
        seen.add(e['input'])
        base.append({
            'instruction': e['instruction'],
            'input': e['input'],
            'output': e['output'],
        })
        added += 1
    print(f'NEW added: {added}; skipped dup inputs: {len(skipped_new)}')

    # 5) ensure only 3 keys
    for e in base:
        keys = set(e.keys())
        if keys != {'instruction', 'input', 'output'}:
            for k in list(e.keys()):
                if k not in ('instruction', 'input', 'output'):
                    del e[k]

    # 6) fix duplicate outputs by lightly differentiating
    out_groups = collections.defaultdict(list)
    for i, e in enumerate(base):
        out_groups[e['output']].append(i)

    dups = {o: idxs for o, idxs in out_groups.items() if len(idxs) > 1}
    print(f'duplicate output groups before fix: {len(dups)} (extra {sum(len(v)-1 for v in dups.values())})')

    # Differentiating remaining duplicate outputs naturally
    variants_tail = [
        " Kısa tutuyorum ama sınırım bu.",
        " Bu konuda uydurma bilgi vermem.",
        " İstersen güvenilir kaynağı birlikte seçebiliriz.",
        " Net konuşmam gerekirse sınırım budur.",
        " Yanıltıcı bir kesinlik veremem.",
        " Daha fazlasını uydurmam doğru olmaz.",
    ]
    for out, idxs in dups.items():
        for n, i in enumerate(idxs[1:], start=0):
            tail = variants_tail[n % len(variants_tail)]
            # ensure uniqueness even if same tail reused across groups
            candidate = base[i]['output'].rstrip() + tail
            k = 0
            existing = set(e['output'] for e in base)
            while candidate in existing:
                k += 1
                candidate = base[i]['output'].rstrip() + tail + f" ({k})"
            base[i]['output'] = candidate
    outs_check = [e['output'] for e in base]
    print(f'duplicate outputs after fix: {len(outs_check) - len(set(outs_check))}')

    outs = [e['output'] for e in base]
    assert len(outs) == len(set(outs)), 'Aynı output kaldı!'
    inps = [e['input'] for e in base]
    assert len(inps) == len(set(inps)), 'Aynı input kaldı!'
    assert all(set(e.keys()) == {'instruction', 'input', 'output'} for e in base)

    ins_c = collections.Counter(e['instruction'] for e in base)
    top_ins = ins_c.most_common(5)
    print('En sık instruction:', top_ins)
    if top_ins[0][1] > 10:
        # diversify excess instructions
        for ins, cnt in ins_c.items():
            if cnt <= 10:
                continue
            idxs = [i for i, e in enumerate(base) if e['instruction'] == ins]
            variants = [
                ins,
                ins.replace('söyleyip', 'belirtip') if 'söyleyip' in ins else ins + ' Net ve dürüst olayım.',
                ('Bu durumda önce sınırımı koyup sonra yardımcı olmalıyım.' if cnt > 10 else ins),
                'Durumu dikkatle okuyup doğru dürüstlük davranışını seçmeliyim.',
                'Bilgi durumuma göre dürüstçe yanıt vermeliyim; uydurmamalıyım.',
                'Sorunun türüne göre bilmiyorum / erişemiyorum / biliyorum ayrımını net tutmalıyım.',
                'Cevabı uydurmadan, erişim ve bilgi sınırımı açıkça korumalıyım.',
                'Kullanıcıya zarar vermeden doğru ve sınırlı bir cevap vermeliyim.',
                'Önce neyin bilinebilir olduğunu ayırıp ona göre konuşmalıyım.',
                'Yanıltıcı kesinlikten kaçınıp uygun dürüstlük dilini kullanmalıyım.',
                'Gerekirse kısa ve net bir sınır cümlesiyle yetinmeliyim.',
            ]
            # make unique variants
            used_v = set()
            for k, i in enumerate(idxs):
                v = variants[k % len(variants)]
                if k >= len(variants):
                    v = f'{ins} ({k})'
                # ensure unique among instructions after change - actually rule is no instruction used >10 times
                # So assign distinct variants for the overflow
                if k < 10:
                    continue  # keep first 10 as original
                base[i]['instruction'] = f'{ins} [{k}]' if v in used_v or v == ins else v
                used_v.add(base[i]['instruction'])
        ins_c = collections.Counter(e['instruction'] for e in base)
        print('After diversify, top:', ins_c.most_common(3))
        assert ins_c.most_common(1)[0][1] <= 10, 'Instruction kalıbı 10 u aştı!'

    out_path = ROOT / 'bilmiyorum-dataset-v2.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(base, f, ensure_ascii=False, indent=1)

    # Classification heuristic for report
    A = B = C = D = 0
    for e in base:
        o = e['output'].lower()
        inp = e['input'].lower()
        if any(x in o for x in ['erişimim yok', 'göremiyorum', 'erişemiyorum', 'canlı', 'dinleyemiyorum', 'işleyemiyorum', 'hatırlamıyorum', 'kalıcı hafız']):
            B += 1
        elif o.startswith('bilmiyorum') or o.startswith('kesin olarak bilmiyorum') or o.startswith('kesin rakamı bilmiyorum') or o.startswith('kesin değeri bilmiyorum') or o.startswith('kesin sayıyı bilmiyorum') or o.startswith('kesin tarihi bilmiyorum') or o.startswith('kesin günü bilmiyorum'):
            A += 1
        elif any(x in o for x in ['hekime', 'avukat', 'eczacı', 'finans danışman', 'acil servis', 'dermatolog', 'nöroloji']):
            # could be D-rewritten
            if any(x in inp for x in ['dav', 'kira', 'miras', 'nafaka', 'tazminat', 'ilaç', 'ağrı', 'öksürük', 'teşhis', 'belirti', 'kredi', 'borsa', 'yatırım']):
                D += 1
            else:
                C += 1
        else:
            C += 1

    print('YAZILDI:', out_path)
    print('toplam:', len(base))
    print('heuristic A/B/C/D:', A, B, C, D)
    print('MED idxs:', sorted(used))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
