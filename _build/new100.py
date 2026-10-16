# -*- coding: utf-8 -*-
NEW100 = [
    {
        'instruction': 'Bilinen bir yapıt soruluyor; evet diyip kısa ve doğru anlatabilirim.',
        'input': "İstanbul Boğazı'nın iki yakayı birleştiren ilk köprüsünü biliyor musun?",
        'output': "Evet, biliyorum. 1973'te açılan Boğaziçi Köprüsü, İstanbul'un iki yakasını ilk kez birleştiren asma köprüdür; 2016'dan sonra resmî adı 15 Temmuz Şehitler Köprüsü olarak değiştirilmiştir.",
    },
    {
        'instruction': 'Tarihî saray soruluyor; bilgiyi verip bir detay ekleyebilirim.',
        'input': "Topkapı Sarayı'nı biliyor musun?",
        'output': "Evet, biliyorum. 1478'de tamamlanan Topkapı Sarayı, Osmanlı İmparatorluğu'nun yaklaşık 400 yıl boyunca idare merkeziydi; İstanbul'un tarihi alanlarıyla birlikte UNESCO Dünya Mirası Listesi'ndedir.",
    },
    {
        'instruction': "Mimar Sinan'ın ustalık eseri soruluyor; kesin bilgiyi aktarabilirim.",
        'input': "Selimiye Camii'ni biliyor musun?",
        'output': "Evet, biliyorum. Edirne'deki Selimiye Camii, Mimar Sinan'ın 1575'te tamamladığı 'ustalık eserim' dediği yapıdır; kubbesiyle Osmanlı mimarisinin zirvesi kabul edilir ve UNESCO listesindedir.",
    },
    {
        'instruction': 'Anıt mezar bilgisi soruluyor; doğru cevabı rahat verebilirim.',
        'input': "Anıtkabir'in mimarını biliyor musun?",
        'output': "Evet, biliyorum. Anıtkabir'in mimarları Emin Onat ve Orhan Arda'dır; yapı 1944'te temeli atılarak 1953'te tamamlanmış ve Atatürk'ün mozolesi buradadır.",
    },
    {
        'instruction': 'Antik kent sorusu; bilinen bilgiyi verebilirim.',
        'input': 'Truva antik kentini biliyor musun?',
        'output': "Evet, biliyorum. Çanakkale'nin Hisarlık'taki Truva, Homeros'un İlyada destanına konu olan ve 9 katman hâlinde kurulmuş bir antik kenttir; 1871'de Heinrich Schliemann'ın kazılarıyla ünlenmiştir.",
    },
    {
        'instruction': 'Arkeolojik kazı yeri soruluyor; bildiğimi söyleyip özetleyebilirim.',
        'input': "Çatalhöyük'ü biliyor musun?",
        'output': "Evet, biliyorum. Konya yakınlarındaki Çatalhöyük, MÖ 7. bine tarihlenen ve çıplak gözle görülür tapınağıyla tanınan bir Neolitik yerleşimdir; UNESCO Dünya Mirası Listesi'ndedir.",
    },
    {
        'instruction': 'Hitit başkenti soruluyor; kesin bilgi verebilirim.',
        'input': "Hattuşa'yı biliyor musun?",
        'output': "Evet, biliyorum. Hitit İmparatorluğu'nun başkenti Hattuşa, Çorum yakınlarındadır; surları, kapıları ve yazıtlarıyla MÖ 2. binyılın başkentidir ve UNESCO listesindedir.",
    },
    {
        'instruction': 'Efsanevi kral ve şehir soruluyor; bilgiyi anlatabilirim.',
        'input': "Midas'ın başkentini biliyor musun?",
        'output': "Evet, biliyorum. Frig Kralı Midas'ın başkenti Gordion'dur; bugün Ankara'nın Polatlı ilçesi yakınlarındadır ve ünlü 'Gordion düğümü' efsanesi buradadır.",
    },
    {
        'instruction': 'Antik tiyatro soruluyor; bilinen gerçeği söyleyebilirim.',
        'input': 'Aspendos tiyatrosunu biliyor musun?',
        'output': "Evet, biliyorum. Antalya'daki Aspendos tiyatrosu, Roma döneminden günümüze en iyi korunmuş antik tiyatrolardan biridir; günümüzde hâlâ konser ve festival sahnesi olarak kullanılır.",
    },
    {
        'instruction': 'Likya kenti soruluyor; bildiğimi belirtip kısaca anlatabilirim.',
        'input': 'Side antik kentini biliyor musun?',
        'output': "Evet, biliyorum. Antalya'daki Side, denize uzanan yarımadada kurulmuş bir Liman kentidir; Apollon Tapınağı ve tiyatrosuyla ünlüdür ve adı 'nar' anlamına gelir.",
    },
    {
        'instruction': 'Mağara bilgisi soruluyor; doğru bilgiyi verebilirim.',
        'input': "Karain Mağarası'nı biliyor musun?",
        'output': "Evet, biliyorum. Antalya'daki Karain Mağarası, Türkiye'de yapılan sistemli kazıların en eskilerindendir; 500 bin yıllık buluntularıyla bilinen bir paleolitik yaşam alanıdır.",
    },
    {
        'instruction': 'Osmanlı dönemi kent dokusu soruluyor; bilgiyi verebilirim.',
        'input': "Safranbolu'yu biliyor musun?",
        'output': "Evet, biliyorum. Karabük'e bağlı Safranbolu, Osmanlı kent dokusunun korunduğu ahşap konaklarıyla ünlüdür; 1994'te UNESCO Dünya Mirası Listesi'ne giren Türkiye'nin ilk yerleşim yerlerinden biridir.",
    },
    {
        'instruction': 'Anadolu Selçuklu eseri soruluyor; kesin bilgi verebilirim.',
        'input': "Divriği Ulu Camii'ni biliyor musun?",
        'output': "Evet, biliyorum. Sivas'taki Divriği Ulu Camii ve Darüşşifası, 1228'de inşa edilmiş ve üç boyutlu taş işçiliğiyle ünlüdür; 1985'te UNESCO listesine giren ilk Türk yapılarından biridir.",
    },
    {
        'instruction': 'İlk Osmanlı başkentinin camisi soruluyor; bilgiyi aktarabilirim.',
        'input': "Bursa Ulu Camii'ni biliyor musun?",
        'output': "Evet, biliyorum. 1399'da Yıldırım Bayezid tarafından yaptırılan Bursa Ulu Camii, erken Osmanlı mimarisinin başyapıtlarındandır; yirmi kubbesiyle 'kubbelerin sultanı' olarak anılır.",
    },
    {
        'instruction': 'Tasavvuf merkezi soruluyor; bildiğimi söyleyip anlatabilirim.',
        'input': "Mevlana Türbesi'ni biliyor musun?",
        'output': "Evet, biliyorum. Konya'daki Mevlana Türbesi, 13. yüzyıl filozof ve şairi Mevlana Celaleddin Rumi'nin kabrinin bulunduğu yapıdır; yeşil kubbesiyle Türkiye'nin en çok ziyaret edilen türbelerindendir.",
    },
    {
        'instruction': 'Halk hikâye kahramanı soruluyor; genel kültür bilgisini verebilirim.',
        'input': "Nasreddin Hoca'ya ait fıkraları biliyor musun?",
        'output': "Evet, biliyorum. Nasreddin Hoca, 13. yüzyılda yaşadığı kabul edilen ve esprili hikâyeleriyle dünya mirasına karışmış bir halk bilgesidir; 'Ya tutarsa' ve 'komşu komşunun külüne muhtaç' gibi fıkralarıyla tanınır.",
    },
    {
        'instruction': 'Türk tasavvuf şairi soruluyor; bilgiyi rahatça verebilirim.',
        'input': "Yunus Emre'yi biliyor musun?",
        'output': "Evet, biliyorum. 13-14. yüzyılda yaşayan Yunus Emre, Anadolu Türkçesiyle yazdığı tasavvuf şiirleriyle halk edebiyatının temel isimlerindendir; 'Sevelim sevilelim' dizeleriyle tanınır.",
    },
    {
        'instruction': 'Halk ozanı soruluyor; doğru bilgiyi verebilirim.',
        'input': "Pir Sultan Abdal'ı biliyor musun?",
        'output': 'Evet, biliyorum. 16. yüzyılda yaşayan Pir Sultan Abdal, alevilik-bektaşilik geleneğinin büyük ozanlarından biridir; direniş ve aşk temalı deyişleriyle bugün de okunur.',
    },
    {
        'instruction': 'Destan kahramanı soruluyor; bilgiyi kısaca anlatabilirim.',
        'input': "Köroğlu'nu biliyor musun?",
        'output': "Evet, biliyorum. Köroğlu, adalet ve sevgi için mücadele eden bir halk kahramanıdır; destanı Türkiye, Azerbaycan ve İran'da ortak olarak söylenegelir ve 2010'da UNESCO listesine girmiştir.",
    },
    {
        'instruction': 'Klasik edebiyat bilgisi soruluyor; net cevap verebilirim.',
        'input': "Kelile ve Dimne'yi biliyor musun?",
        'output': "Evet, biliyorum. Efsanevi vezir Beydeba'ya atfedilen Kelile ve Dimne, hayvan hikâyeleriyle yönetim ahlakı öğütleyen bir eserdir; Sanskritçe kökenli hayvan masallarının Arapça üzerinden Türkçeye uyarlanmış ahlakî bir hikâye derlemesidir.",
    },
    {
        'instruction': 'Divan şairi soruluyor; bilgiyi verebilirim.',
        'input': "Nedim'i biliyor musun?",
        'output': "Evet, biliyorum. 18. yüzyıl divan şairi Nedim, şehir hayatını ve sevgiyi işlediği şiirleriyle Lale Devri'nin simgesidir; şarkılara uyarlanan 'Bülbül' kasidesiyle tanınır.",
    },
    {
        'instruction': 'Tasavvuf klasiği soruluyor; doğru bilgiyi aktarabilirim.',
        'input': "Şeyh Galib'in Hüsn ü Aşk'ını biliyor musun?",
        'output': "Evet, biliyorum. 1782'de yazılan Hüsn ü Aşk, Şeyh Galib'in tasavvufi alegorik mesnevisidir; Hüsn (güzellik) ile Aşk'ın yolculuğunu anlatan bu eser son dönem divan edebiyatının zirvesi sayılır.",
    },
    {
        'instruction': 'Servet-i Fünun romanı soruluyor; bilgiyi verebilirim.',
        'input': "Mai ve Siyah'ı biliyor musun?",
        'output': "Evet, biliyorum. Halit Ziya Uşaklıgil'in 1897'de yayımladığı Mai ve Siyah, Servet-i Fünun döneminin temel romanlarındandır; sanatçı kişiliğin çatışmalarını anlatmasıyla bilinir.",
    },
    {
        'instruction': 'Cumhuriyet dönemi romanı soruluyor; kısaca anlatabilirim.',
        'input': "Acımak'ı biliyor musun?",
        'output': "Evet, biliyorum. Reşat Nuri Güntekin'in 1928 tarihli romanı Acımak, bir öğretmenin geçmişte bir öğrencisine yaptığı haksızlığı fark edişini anlatır; vicdan ve pişmanlık temasıyla öne çıkar.",
    },
    {
        'instruction': 'Erken Cumhuriyet romanı soruluyor; bilgiyi verebilirim.',
        'input': "Sinekli Bakkal'ı biliyor musun?",
        'output': "Evet, biliyorum. Halide Edip Adıvar'ın 1936'da yazdığı Sinekli Bakkal, savaş yılları İstanbul'unu ve bir bakkalın çevresindeki mahalle insanlarını anlatır; yazarın en çok okunan eserlerinden biridir.",
    },
    {
        'instruction': 'Köy romanı soruluyor; doğru bilgiyi verebilirim.',
        'input': "Bereketli Topraklar Üzerinde'yi biliyor musun?",
        'output': "Evet, biliyorum. Orhan Kemal'in 1954 tarihli romanı Bereketli Topraklar Üzerinde, Çukurova'ya işçi olarak giden bir ailenin mücadelesini anlatır; Türk edebiyatının gerçekçi köy-şehir karşıtlığının başyapıtlarındandır.",
    },
    {
        'instruction': 'Dünya edebiyatı sorusu; rahatlıkla cevaplayabilirim.',
        'input': "Hamlet'i biliyor musun?",
        'output': "Evet, biliyorum. Shakespeare'in 1600 civarında yazdığı Hamlet, 'olmak ya da olmamak' monoloğuyla ünlü bir intikam tragedyaasıdır; dünya edebiyatının en çok yorumlanan oyunlarından biridir.",
    },
    {
        'instruction': 'Dünya klasikleri soruluyor; bilgiyi özetleyebilirim.',
        'input': "Don Kişot'u biliyor musun?",
        'output': "Evet, biliyorum. Cervantes'in 1605 ve 1615'te iki cilt hâlinde yayımladığı Don Kişot, şövalye romanlarını taşlayan ve modern romanın öncüsü sayılan eserdir; idealizm ile gerçeklik arasındaki çatışmayı anlatır.",
    },
    {
        'instruction': 'Fransız klasikleri soruluyor; kısaca anlatabilirim.',
        'input': "Sefiller'i biliyor musun?",
        'output': "Evet, biliyorum. Victor Hugo'nun 1862'de yayımladığı Sefiller, Jean Valjean'ın yaşamı üzerinden adalet, ahlak ve toplumsal eşitsizliği anlatan devasa bir romandır; dünyanın en çok okunan eserlerindendir.",
    },
    {
        'instruction': 'Modern fantastik soruluyor; bilgiyi verebilirim.',
        'input': "Yüzüklerin Efendisi'ni biliyor musun?",
        'output': "Evet, biliyorum. J.R.R. Tolkien'in 1954-55'te yayımlanan üçlemesi, Orta Dünya evreninde geçer ve modern fantastik edebiyatın temel taşı sayılır; film üçlemesiyle de dünya çapında tanınmıştır.",
    },
    {
        'instruction': 'Çağdaş edebiyat sorusu; cevap verebilirim.',
        'input': "1984'ü biliyor musun?",
        'output': "Evet, biliyorum. George Orwell'in 1949'da yazdığı 1984, totaliter bir gelecekte geçen distopik romandır; 'Büyük Birader' kavramı ve gözetim toplumu eleştirisiyle edebiyatın en etkili eserlerindendir.",
    },
    {
        'instruction': 'Bilim kurgu sorusu; bilgiyi anlatabilirim.',
        'input': "Dune'u biliyor musun?",
        'output': "Evet, biliyorum. Frank Herbert'ın 1965'te yayımladığı Dune, çöl gezegeni Arrakis'te geçen ve ekoloji, politika ve din temalarını işleyen bir bilim kurgu klasiğidir; türünün en çok satanlarındandır.",
    },
    {
        'instruction': 'Polisiye edebiyatı sorusu; net cevap verebilirim.',
        'input': "Sherlock Holmes'u biliyor musun?",
        'output': "Evet, biliyorum. Arthur Conan Doyle'un yarattığı Sherlock Holmes, dedektif edebiyatının en ünlü karakteridir; 19. yüzyıl Londra'sında geçen maceraları ve gözlem ve mantık yürütme yöntemiyle tanınır.",
    },
    {
        'instruction': 'Polisiye kraliçesi soruluyor; bilgiyi verebilirim.',
        'input': "Agatha Christie'yi biliyor musun?",
        'output': "Evet, biliyorum. Agatha Christie, dünyanın en çok satan polisiye yazarıdır; Hercule Poirot ve Miss Marple karakterleriyle 'On Küçük Zenci' ve 'Doğu Ekspresinde Cinayet' gibi klasikler yazmıştır.",
    },
    {
        'instruction': 'Amerikan edebiyatı sorusu; kısaca anlatabilirim.',
        'input': "Ernest Hemingway'i biliyor musun?",
        'output': "Evet, biliyorum. Ernest Hemingway, 1954 Nobel Edebiyat Ödülü sahibi Amerikalı yazardır; 'Yaşlı Adam ve Deniz' ile Pulitzer, Nobel ile ödüllendirilmiş ve sade üslubuyla edebiyatı değiştirmiştir.",
    },
    {
        'instruction': 'Latin Amerikan edebiyatı sorusu; cevaplayabilirim.',
        'input': "Gabriel García Márquez'i biliyor musun?",
        'output': "Evet, biliyorum. Kolombiyalı yazar García Márquez, 'büyülü gerçekçilik' akımının kurucularındandır; 'Yüzyıllık Yalnızlık' romanıyla 1982'de Nobel Edebiyat Ödülü'nü kazanmıştır.",
    },
    {
        'instruction': 'Varoluşçu yazar soruluyor; bilgiyi verebilirim.',
        'input': "Albert Camus'nun Yabancı'sını biliyor musun?",
        'output': "Evet, biliyorum. 1942'de yayımlanan Yabancı, absürdizm felsefesinin edebiyattaki karşılıklarından biridir; Meursault karakteri üzerinden toplumsal uyum sorgulaması yapar.",
    },
    {
        'instruction': 'Rus klasikleri soruluyor; kısaca anlatabilirim.',
        'input': "Suç ve Ceza'yı biliyor musun?",
        'output': "Evet, biliyorum. Dostoyevski'nin 1866'da yayımladığı Suç ve Ceza, yoksul öğrenci Raskolnikov'un işlediği cinayet ve vicdan muhasebesini anlatır; psikolojik derinliğiyle dünya edebiyatının en etkili romanlarındandır.",
    },
    {
        'instruction': 'Rus edebiyatı soruluyor; bilgiyi aktarabilirim.',
        'input': "Anna Karenina'yı biliyor musun?",
        'output': "Evet, biliyorum. Tolstoy'un 1878'de yayımladığı Anna Karenina, evlilik, aşk ve toplum kuralları arasında sıkışan bir kadının trajedisini anlatır; 'Bütün mutlu aileler birbirine benzer' cümlesiyle açılır.",
    },
    {
        'instruction': 'İcat tarihi soruluyor; kesin bilgi verebilirim.',
        'input': "Gutenberg'in matbaasını biliyor musun?",
        'output': "Evet, biliyorum. Johannes Gutenberg, 1440 civarında Avrupa'da hareketli metal harflerle matbaa kullanımını geliştirdi; bu buluş bilgiyi kitlesel olarak çoğaltmayı mümkün kılarak Rönesans'ı hızlandırdı.",
    },
    {
        'instruction': 'Sanat tarihi soruluyor; bilgiyi verebilirim.',
        'input': "Son Akşam Yemeği'ni biliyor musun?",
        'output': "Evet, biliyorum. Leonardo da Vinci'nin Milano'daki Santa Maria delle Grazie kilisesinin duvarına yaptığı fresk, İsa'nın havarilerle son yemeğini anlatır; Hristiyan sanatının en ünlü betimlemelerinden biridir.",
    },
    {
        'instruction': 'Bilim kavramı soruluyor; anlatabilirim.',
        'input': 'Turing testini biliyor musun?',
        'output': "Evet, biliyorum. Alan Turing'in 1950'de önerdiği test, bir makinenin insan gibi davranıp davranmadığını değerlendirir; yapay zekâ felsefesinin temel tartışmalarından biridir.",
    },
    {
        'instruction': 'Temel fizik soruluyor; bildiğimi söyleyebilirim.',
        'input': "Newton'un hareket yasalarını biliyor musun?",
        'output': "Evet, biliyorum. Newton'un üç hareket yasası; atalet, kuvvet ile ivme (F=ma) ve etki-tepki ilkesini tanımlar. Klasik mekaniğin temelini oluşturur ve günlük hızlar için bugün de geçerlidir.",
    },
    {
        'instruction': 'Biyoloji bilgisi soruluyor; doğru cevabı verebilirim.',
        'input': "DNA'nın çift sarmal yapısını biliyor musun?",
        'output': "Evet, biliyorum. DNA, Watson ve Crick'in 1953'te açıkladığı çift sarmal yapıdadır; dört baz (A, T, G, C) iplikler arasında eşleşerek genetik bilgiyi saklar.",
    },
    {
        'instruction': 'Havacılık tarihi soruluyor; bilgiyi verebilirim.',
        'input': 'İlk motorlu uçuşu biliyor musun?',
        'output': "Evet, biliyorum. Wright Kardeşler, 17 Aralık 1903'te Kitty Hawk'ta 'Flyer' adlı uçakla 12 saniyelik ilk kontrollü motorlu uçuşu gerçekleştirdi; havacılığın başlangıcı sayılır.",
    },
    {
        'instruction': 'Bilimsel birim soruluyor; kesin bilgi verebilirim.',
        'input': 'Ampulün icadını biliyor musun?',
        'output': "Evet, biliyorum. Thomas Edison, 1879'da karbon filamanlı, uzun ömürlü ve ticari kullanılabilir ampulü geliştirdi; elektrikli aydınlatmayı evlere taşıyan isim olarak tarihe geçti.",
    },
    {
        'instruction': 'Coğrafya bilgisi soruluyor; bildiğimi belirtebilirim.',
        'input': "Bosphorus'un dünyadaki benzerlerini biliyor musun?",
        'output': "Evet, biliyorum. Boğazlar genellikle iki kıtayı ayıran dar su geçitleridir; İstanbul Boğazı Avrupa ile Asya'yı ayıran stratejik bir su yoludur; benzer boğazlara Çanakkale Boğazı ve Cebelitarık Boğazı örnek verilebilir.",
    },
    {
        'instruction': 'Matematik tarihi soruluyor; bilgiyi verebilirim.',
        'input': 'Pisagor teoremini biliyor musun?',
        'output': 'Evet, biliyorum. Pisagor teoremi, dik üçgende hipotenüsün karesinin dik kenarların kareleri toplamına eşit olduğunu söyler (a²+b²=c²); antik çağdan beri geometrinin temelidir.',
    },
    {
        'instruction': 'Tarihî figür soruluyor; kısaca anlatabilirim.',
        'input': "Marie Curie'yi biliyor musun?",
        'output': 'Evet, biliyorum. Marie Curie, radyum ve polonyum elementlerini keşfeden iki dalda Nobel ödülü kazanan ilk bilim insanıdır (1903 Fizik, 1911 Kimya); radyoaktivite araştırmalarının öncüsüdür.',
    },
    {
        'instruction': 'Çevre bilgisi soruluyor; doğru bilgiyi aktarabilirim.',
        'input': 'Ozon tabakasını biliyor musun?',
        'output': "Evet, biliyorum. Ozon tabakası, stratosferde Güneş'ten gelen zararlı morötesi ışınları süzen bir gaz tabakasıdır; 1980'lerdeki incelmesi Montreal Protokolü ile uluslararası iş birliğiyle durdurulmuştur.",
    },
    {
        'instruction': 'Ekonomi kavramı soruluyor; bilgiyi anlatabilirim.',
        'input': 'Enflasyonu biliyor musun?',
        'output': 'Evet, biliyorum. Enflasyon, genel fiyat düzeyinin zamanla artması ve paranın alım gücünün düşmesidir; genelde yüzde olarak yıllık olarak ölçülür ve merkez bankalarının temel takip ettiği göstergedir.',
    },
    {
        'instruction': 'Borsa kavramı soruluyor; bilgiyi verebilirim.',
        'input': 'Borsa endeksi nedir, biliyor musun?',
        'output': 'Evet, biliyorum. Borsa endeksi, belli bir grup hissenin fiyat değişimini özetleyen göstergedir; BIST 100 örneğinde olduğu gibi piyasanın genel yönü hakkında fikir verir.',
    },
    {
        'instruction': 'Tarih bilgisi soruluyor; net cevap verebilirim.',
        'input': "Kurtuluş Savaşı'nın başlangıcını biliyor musun?",
        'output': "Evet, biliyorum. Millî Mücadele, 1919'da Mustafa Kemal'in Samsun'a çıkmasıyla fiilen başladı; 23 Nisan 1920'de TBMM'nin açılmasıyla kurumsal temelini attı.",
    },
    {
        'instruction': 'Gelecek turnuva sonucu soruluyor; sonuç belirsiz, bilmiyorum demeliyim.',
        'input': "2040 FIFA Dünya Kupası'nı hangi ülke kazanır, biliyor musun?",
        'output': 'Bilmiyorum; turnuva henüz oynanmadı ve on beş yıllık futbol gelişimi, kadrolar ve şans sonucu belirleyeceği için kazananı şimdiden bilemek imkânsızdır.',
    },
    {
        'instruction': 'Gelecek seçim sonucu soruluyor; bunu kimse önceden bilemez.',
        'input': 'Bir sonraki genel seçimleri hangi parti kazanır, biliyor musun?',
        'output': 'Bilmiyorum; seçim sonuçları kampanya döneminin gidişatına ve seçmen tercihine bağlıdır, sandık açılmadan kesin konuşmak mümkün değildir.',
    },
    {
        'instruction': 'Gelecek ödül kazananı soruluyor; açıklanmadan bilinemez.',
        'input': "2027 Nobel Fizik Ödülü'nü kim alır, biliyor musun?",
        'output': 'Bilmiyorum; Nobel komitesi kararını açıklayana kadar adaylar bile gizli tutulduğu için kazananı önceden kimse bilemez.',
    },
    {
        'instruction': 'Rastgele çekiliş sorusu; kimsenin bilemeyeceğini söylemeliyim.',
        'input': "On Numara'nın bu haftaki kazanan kolonunu biliyor musun?",
        'output': 'Bilmiyorum; sayılar rastgele çekildiği için sonuç önceden bilinemez. Böyle bir iddiada bulunan kişilerden uzak durmanı öneririm.',
    },
    {
        'instruction': 'Bir yıllık kur hedefi soruluyor; belirsiz, bilmiyorum demeliyim.',
        'input': 'Seneye bugün dolar kaç lira olur, biliyor musun?',
        'output': 'Bilmiyorum; bir yıl sonraki kur, faiz, enflasyon ve küresel gelişmelere bağlı olarak değişir ve önceden kesin kestirilemez.',
    },
    {
        'instruction': 'Uzun vadeli teknoloji tahmini; spekülasyon alanı, bilmiyorum demeliyim.',
        'input': 'Yirmi yıl sonra cep telefonları tamamen nasıl olacak, biliyor musun?',
        'output': 'Kesin olarak bilmiyorum; teknolojinin yirmi yıllık gelişimi bugünden öngörülemez. Geçmişteki değişim hızına bakarak tahmin yürütülebilir ama bu kesin bilgi değildir.',
    },
    {
        'instruction': 'Gelecekteki zenginlik sıralaması soruluyor; bilinemez.',
        'input': 'On yıl sonra dünyanın en zengin insanı kim olacak, biliyor musun?',
        'output': 'Bilmiyorum; servet sıralaması piyasa değerlerine, şirket performanslarına ve kişisel kararlara bağlı olarak sürekli değişir.',
    },
    {
        'instruction': 'Gelecek olimpiyat sonucu; bilinemez.',
        'input': "2032 Brisbane Olimpiyatları'nda 100 metre finalini kim kazanır, biliyor musun?",
        'output': 'Bilmiyorum; sekiz yıl sonraki atlet kadroları ve form durumu belirsizdir, sonucu şimdiden kestirmek imkânsızdır.',
    },
    {
        'instruction': 'Gelecekteki seçim takvimi belirsiz; uydurmamalıyım.',
        'input': "Türkiye'de bir sonraki genel seçim ne zaman yapılacak, biliyor musun?",
        'output': 'Kesin tarihi bilmiyorum; seçim takvimi yasal süreçlere ve siyasi gelişmelere bağlı olarak değişebilir. Resmi açıklamalar dışındaki tarihler spekülasyondur.',
    },
    {
        'instruction': 'Dünya kupası kazananı soruluyor; turnuva oynanmadan bilinemez.',
        'input': "Bir sonraki FIFA Dünya Kupası'nı hangi ülke kazanır, biliyor musun?",
        'output': 'Bilmiyorum; kazanan, turnuvadaki performanslarla belli olur ve kadrolar netleşmeden tahmin yürütmek güvenilmezdir.',
    },
    {
        'instruction': 'Yapay zekâ eşiği iddiası; kesin tarih bilinemez.',
        'input': 'Yapay zekânın insan zekâsını geçeceği kesin tarihi biliyor musun?',
        'output': 'Bilmiyorum; bu konuda uzmanlar arasında bile uzlaşı yok ve kesin bir takvim veren her iddia spekülasyondur. Bazı tahminler var ama hiçbiri bilgi değildir.',
    },
    {
        'instruction': 'Gelecekteki nüfus rakamı kesin değil; senaryo ile kesin değeri ayırmalıyım.',
        'input': "2050'de dünya nüfusu kesin olarak kaç milyar olacak, biliyor musun?",
        'output': 'Kesin rakamı bilmiyorum; BM projeksiyonları yaklaşık 9-10 milyar aralığında senaryolar üretiyor ama bunlar kesin gelecek değil, olasılık tahminleridir.',
    },
    {
        'instruction': 'Doğal afetin zamanı bilinemez; uydurmamalıyım.',
        'input': "İzmir'deki bir sonraki büyük depremin tarihini biliyor musun?",
        'output': 'Bilmiyorum; depremin gününü ne bilim ne de teknoloji kesin öngörebiliyor. Bilinen, fay hattının aktif olması ve hazırlıklı olunması gerektiğidir.',
    },
    {
        'instruction': 'Kişisel yaşam tercihi soruluyor; gelecekteki tercihler bilinemez.',
        'input': 'Hayatının geri kalanında en çok hangi şehirde yaşayacaksın, biliyor musun?',
        'output': 'Bilmiyorum; bu senin gelecekteki kararlarına ve hayat koşullarına bağlı bir durum, önceden bilinemez.',
    },
    {
        'instruction': 'Teknolojik devrimin tarihi belirsiz; bilmiyorum demeliyim.',
        'input': 'Bir sonraki büyük teknolojik devrim ne zaman başlayacak, biliyor musun?',
        'output': 'Bilmiyorum; tarihsel olarak teknik devrimler geriye dönük olarak adlandırılır ve başlangıç anları önceden kestirilemez.',
    },
    {
        'instruction': 'Gelecekteki eğitim politikası bilinemez.',
        'input': "2040'ta okullarda hangi yabancı dil zorunlu olacak, biliyor musun?",
        'output': 'Bilmiyorum; eğitim politikaları dönemin iktidarlarınca belirlenir ve on beş yıl sonrası için kesin konuşmak mümkün değildir.',
    },
    {
        'instruction': 'Mars görevi takvimi belirsiz; kesin bilgi yok.',
        'input': 'Hangi ülke ilk insanlı Mars görevini gerçekleştirecek, biliyor musun?',
        'output': 'Bilmiyorum; hem tarih hem de ülke henüz kesinleşmedi. Ajansların hedef tarihleri sık revize ediliyor ve bu yüzden kesin bilgi değil, planlamadır.',
    },
    {
        'instruction': 'Gelecek salgının zamanı öngörülemez.',
        'input': 'Dünyanın bir sonraki büyük salgını ne zaman olacak, biliyor musun?',
        'output': 'Bilmiyorum; salgınlar yeni patojenlerin ortaya çıkışına bağlıdır ve bunun zamanı önceden bilinemez. Bilim, risk azaltmaya çalışır ama takvim veremez.',
    },
    {
        'instruction': 'Kişisel emeklilik yaşının geleceği bilinemez.',
        'input': 'Senin emeklilik yaşın kaç olacak, biliyor musun?',
        'output': 'Bilmiyorum; emeklilik yaşı yasal düzenlemelerle değişebilir ve senin çalışma geçmişinle birlikte netleşir, şimdiden kesin söylenemez.',
    },
    {
        'instruction': 'Çok uzak gelecekteki yönetim merkezi spekülasyon; bilmiyorum demeliyim.',
        'input': "Elli yıl sonra Türkiye'nin başkenti neresi olacak, biliyor musun?",
        'output': 'Bilmiyorum; başkent değişikliği büyük anayasal ve siyasi kararlar gerektirir ve yarım yüzyıl sonrası için kesin konuşmak imkânsızdır.',
    },
    {
        'instruction': 'Gelecekteki kazanç sıralaması belirsiz.',
        'input': 'Önümüzdeki on yılda en çok kazandıran meslek hangisi olacak, biliyor musun?',
        'output': 'Bilmiyorum; kazanç sıralamaları ekonomik döngülere ve teknolojik değişime bağlı olarak değişir, on yıllık kesin tahmin yapılamaz.',
    },
    {
        'instruction': 'Gelecekteki aile tercihi bilinemez.',
        'input': 'Senin çocuklarının isimleri ne olacak, biliyor musun?',
        'output': 'Bilmiyorum; bu senin gelecekteki tercihlerine bağlı bir karar, şimdiden bilemeyeceğim bir bilgi.',
    },
    {
        'instruction': 'Yakın gelecekteki popülerlik sıralaması belirsiz.',
        'input': 'Gelecek ayın en çok izlenen dizisi hangisi olacak, biliyor musun?',
        'output': 'Bilmiyorum; izlenme rakamları yayınlanana kadar bilinemez ve kısa vadede bile sürprizler yaşanır.',
    },
    {
        'instruction': 'Haftalık hisse performansı öngörülemez.',
        'input': 'Gelecek hafta en çok hangi hisse yükselir, biliyor musun?',
        'output': 'Bilmiyorum; haftalık hisse hareketleri kısa vadeli haber akışı ve alıcı-satıcı dengesine göre şekillenir, önceden kesin bilemeyiz.',
    },
    {
        'instruction': 'Ömür süresi kişiye özel ve bilinemez.',
        'input': 'Dünyanın bir sonraki en uzun ömürlü insanının kim olacağını biliyor musun?',
        'output': 'Bilmiyorum; insan ömrü genetik, çevre ve şansa bağlı olarak değişir ve gelecekteki bireylerin yaşam süresi önceden kestirilemez.',
    },
    {
        'instruction': 'Uzun vadeli şirket değeri belirsiz.',
        'input': "2030'da dünyanın en değerli şirketi hangisi olacak, biliyor musun?",
        'output': 'Bilmiyorum; şirket değerlemeleri piyasa koşullarına göre sürekli değişir ve beş yıl sonrası için kesin sıralama yapmak mümkün değildir.',
    },
    {
        'instruction': 'Kişisel sınav sonucu bilinemez.',
        'input': 'Üniversite sınavında Türkiye kaçıncısı olacağımı biliyor musun?',
        'output': 'Bilmiyorum; sonucu belirleyecek performansın ve o günkü koşullar önceden bilinemez. İstersen çalışma planını birlikte gözden geçirebiliriz.',
    },
    {
        'instruction': 'Gelecekteki siber olayın zamanı öngörülemez.',
        'input': 'Bir sonraki büyük siber saldırı ne zaman olacak, biliyor musun?',
        'output': 'Bilmiyorum; siber saldırılar saldırganların kararlarına bağlıdır ve bunun zamanı önceden bilinemez; savunma için güncel kalmaktan başka yol yoktur.',
    },
    {
        'instruction': 'Kurban bayramının gelecekteki takvimi gözleme bağlıdır.',
        'input': "Gelecek yıl Kurban Bayramı'na kaç gün kaldığını kesin biliyor musun?",
        'output': 'Kesin günü bilmiyorum; dini günler hicri takvime göre hesaplanır ve hilalin gözlenmesiyle kesinleşir, bu yüzden birkaç günlük belirsizlik her zaman vardır.',
    },
    {
        'instruction': 'Mars yolculuğunun tarihi kesin değil; bilmiyorum demeliyim.',
        'input': 'İlk insanlı Mars yolculuğu ne zaman yapılacak, biliyor musun?',
        'output': 'Bilmiyorum; ajansların hedef tarihleri var ama bütçe, teknik ve güvenlik gelişmelerine göre sürekli erteleniyor. Kesin tarih vermek mümkün değil.',
    },
    {
        'instruction': 'Mevsimlik rekor günü öngörülemez.',
        'input': 'Önümüzdeki yazın en sıcak günü hangisi olacak, biliyor musun?',
        'output': 'Bilmiyorum; günlük hava tahminleri ancak birkaç gün önceden güvenilir olur ve aylar sonrasının en sıcak günü önceden bilinemez.',
    },
    {
        'instruction': 'Şampiyonlar Ligi kazananı belirsiz.',
        'input': "Önümüzdeki sezon Şampiyonlar Ligi'ni hangi takım kazanır, biliyor musun?",
        'output': 'Bilmiyorum; sezonun transferleri, sakatlıklar ve form durumu sonucu belirleyeceği için kazananı şimdiden bilemeyiz.',
    },
    {
        'instruction': 'Yayın dünyasındaki gelecek belirsiz.',
        'input': 'Gelecek yılın en çok satan kitabı hangisi olacak, biliyor musun?',
        'output': 'Bilmiyorum; satış rakamları yayımlandıkça belli olur ve edebiyat piyasasında sürprizler sık yaşanır.',
    },
    {
        'instruction': 'Kişisel ömür uzunluğu bilinemez.',
        'input': 'Sen kaç yıl yaşayacaksın, biliyor musun?',
        'output': 'Bilmiyorum; insan ömrü sağlık, genetik ve şansa bağlı olarak değişir ve kimse kendi yaşam süresini önceden bilemez.',
    },
    {
        'instruction': 'Ekonomik kriz takvimi öngörülemez.',
        'input': 'Bir sonraki büyük ekonomik kriz ne zaman olacak, biliyor musun?',
        'output': 'Bilmiyorum; ekonomik krizlerin zamanı önceden kestirilemez, ancak risk sinyalleri izlenebilir. Kesin tarih veren her iddiaya şüpheyle yaklaşmak gerekir.',
    },
    {
        'instruction': 'Kişisel en mutlu gün bilinemez.',
        'input': 'Hayatının en mutlu günü hangisi olacak, biliyor musun?',
        'output': 'Bilmiyorum; bu senin gelecekteki deneyimlerine bağlı bir şey, önceden bilinemez.',
    },
    {
        'instruction': 'Konunun bilinen ve bilinmeyen kısmını ayırmalıyım; emin olmadığımı açıkça söylemeliyim.',
        'input': "Ay'ın karanlık yüzü hakkında ne biliyorsun, hepsini biliyor musun?",
        'output': "Bilinen kısım: Ay'ın Dünya'ya dönük olmayan yüzü 1959'daki Sovyet Luna 3 sondasıyla ilk kez görüntülendi ve karasal gözlemlerle haritalandı. Bilinmeyen kısım: derin yeraltı yapısının tamamı ve kutup kraterlerindeki buzun kesin dağılımı hâlâ araştırılıyor; ben bunların tamamını bilmiyorum.",
    },
    {
        'instruction': 'Kısmen biliyorum; keşfedilenle keşfedilmeyeni açıkça ayırmalıyım.',
        'input': 'Dünya okyanuslarının tamamını haritaladık mı, biliyor musun?',
        'output': "Kısmen biliyorum: okyanusların kabaca %80'i hiç detaylı haritalanmadı ve çoğu derin deniz canlısı henüz tanımlanmadı. Yüzey akıntıları ve büyük dağılımlar iyi bilinir ama derinler hâlâ büyük ölçüde keşfedilmemiş durumda.",
    },
    {
        'instruction': 'Kısmen bilgi; bilinen kısmı anlatıp bilinmeyeni işaret etmeliyim.',
        'input': 'İnsan beyninin tamamıyla nasıl çalıştığını biliyor musun?',
        'output': 'Kısmen biliyorum: nöronların elektrokimyasal sinyallerle iletiştiği, bellek ve duyuların hangi bölgelerle ilişkili olduğu biliniyor. Ancak bilincin ve rüyaların tam mekanizması bilimde hâlâ çözülmemiş bir soru; ben de bunu bilmiyorum.',
    },
    {
        'instruction': 'Kısmen bilgi; çözüleni ve çözülmeyeni ayırmalıyım.',
        'input': 'Antik Mısır hiyerogliflerinin tamamını okuyabiliyor muyuz, biliyor musun?',
        'output': "Kısmen biliyorum: 1822'de Champollion'un Rosetta Taşı sayesinde çözümüyle hiyeroglif okunabilir hâle geldi ve çoğu metin çevrilebiliyor. Ancak bazı sembollerin ve kısa yazıtların anlamı hâlâ tartışmalı, yani tamamını bildiğimizi söyleyemem.",
    },
    {
        'instruction': 'Kısmen biliyorum; kesin bilineni ve spekülasyonu ayırmalıyım.',
        'input': "Stonehenge'in neden inşa edildiğini kesin olarak biliyor musun?",
        'output': 'Kısmen biliyorum: MÖ 3000-2000 arasında inşa edildiği ve güneş takvimiyle ilişkili olduğu güçlü bulgularla destekleniyor. Ancak inşa eden topluluğun kimliği ve tam ritüel amacı bilinmiyor; kesin cevap verilemez.',
    },
    {
        'instruction': 'Efsane ile kanıtı ayıran kısmi bilgi sunmalıyım.',
        'input': "Bermuda Şeytan Üçgeni'nin gizemini çözdük mü, biliyor musun?",
        'output': "Kısmen biliyorum: bölgedeki kayıpların büyük bölümünün fırtına ve akıntı gibi doğal nedenlerle açıklandığı biliniyor. Ancak bazı vakalarda tam veri yok ve popüler anlatılar abartılı; 'gizemli kuvvet' iddialarının kanıtı yok, o kısmı bilinmiyor.",
    },
    {
        'instruction': 'Kısmen bilinen konu; bilinen mekanizmayı anlatıp açık sorunu belirtmeliyim.',
        'input': 'Koku alma duyusunun tam mekanizmasını biliyor musun?',
        'output': "Kısmen biliyorum: koku reseptörlerinin sinyalleri beyindeki koku bulgularına ilettiği ve 2004 Nobel Ödülü'yle tanınan bu mekanizmanın temelleri biliniyor. Ancak binlerce kokunun beynin tam olarak nasıl ayırt edildiği hâlâ tam çözülmemiş bir konu.",
    },
    {
        'instruction': 'Kısmen biliyorum; gözlemleneni anlatıp açıklanamayanı söylemeliyim.',
        'input': 'Göçmen kuşların yolunu tam olarak nasıl bulduğunu biliyor musun?',
        'output': 'Kısmen biliyorum: manyetik alan algısı, güneş ve yıldız konumu gibi pek çok yön bulma mekanizmasının birlikte çalıştığı gösterildi. Ancak bazı türlerin binlerce kilometrelik rotayı ilk seferde neredeyse hatasız tamamlamasının tam açıklaması hâlâ araştırma konusu.',
    },
    {
        'instruction': 'Kısmi bilgi; bilinen hipotezleri verip kesin cevabın olmadığını söylemeliyim.',
        'input': 'Neden rüya gördüğümüzü kesin olarak biliyor musun?',
        'output': 'Kısmen biliyorum: rüyaların hafıza pekiştirme, duygu işleme ve beyin aktivitesinin devamı gibi işlevleri üzerine güçlü hipotezler var. Ancak rüyaların kesin evrimsel amacı bilimde hâlâ tartışmalı; kesin bir cevap yok.',
    },
    {
        'instruction': 'Evrenin sınırlı mı sonsuz mu olduğunu kesin bilmiyorum; bilinen çerçeveyi verip sınırı çizmeliyim.',
        'input': 'Evrenin sınırlı mı yoksa sonsuz mu olduğunu biliyor musun?',
        'output': 'Kısmen biliyorum: gözlenebilir evrenin yaklaşık 93 milyar ışık yılı çapında olduğu ölçümlerle biliniyor. Ancak gözlenebilir alanın ötesinin sınırlı mı sonsuz mu olduğu, evrenin topolojisi hakkında kesin bilgi yok; bilim bu soruyu henüz yanıtlayamadı.',
    },
    {
        'instruction': 'Gelecekteki teknoloji ödülü kazananı soruluyor; açıklanmadan bilinemez.',
        'input': "2030 Turing Ödülü'nü kim alır, biliyor musun?",
        'output': 'Bilmiyorum; ödül komitesi kararını açıklayana kadar kazananı önceden kimse bilemez. Tahminler spekülasyondan ibarettir.',
    },
]
