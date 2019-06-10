### Problem - 7 Dünya Bankası Verilerinde Türkiye

Arkadaşlar aşağıdaki iki satır ile Dünya Bankası tarafından sunulan 1960-2017 arasındaki Türkiye'ye ait bazı verilere ulaşabilirsiniz. Nüfus oranı, kişi başı elektrik tüketimi, kişi başı CO2 emisyonu vs. Bunun üzerinde çalışabilirsiniz Pandas ile.

https://gist.github.com/fuatbeser/423af0f32a20387898c72308d0dead28

*Problem 7: Dünya Bankası Verilerinde Türkiye*

Arkadaşlar aşağıdaki iki satır ile Dünya Bankası tarafından sunulan 1960-2017 arasındaki Türkiye'ye ait bazı verilere ulaşabilirsiniz. 

Nüfus oranı, kişi başı elektrik tüketimi, kişi başı CO2 emisyonu vs. Bunun üzerinde çalışabilirsiniz Pandas ile.

https://gist.github.com/fuatbeser/423af0f32a20387898c72308d0dead28

**Türkiye'ye ait şu veriler var:**

```
3     İleri teknoloji ihracatları (üretilen ihracat ...
4     Gayri safi değişim ticaret hadleri indeksi (20...
5                  Mal ithalat ve ihracatı (GSYİH %'si)
6                                         Nüfus, toplam
7                               Nüfus artışı (yıllık %)
8     Doğurganlık oranı, toplam (kadın başına düşen ...
9           Doğumda beklenen yaşam süresi, toplam (yıl)
10       Ölüm oranı, bebek (her 1.000 canlı doğum için)
11    Doğum kontrolü yaygınlık oranı (15-49 yaş aras...
12    Gençlerde doğurganlık oranı (15-19 yaş arası h...
13                                              Net göç
14              İşsizlik, toplam (toplam işgücüne %'si)
15    Ulusal yoksulluk sınırında kalan yoksul insan ...
16                                         GİNİ indeksi
17    Günlük gelir 1,90 doların altında kalan yoksul...
18              En düşük %20'lik gruba düşen gelir payı
19    Yetersiz beslenme yaygınlığı, yaşa göre kilo (...
20    Uzman sağlık personelinin katılımıyla yapılan ...
21    Bağışıklama, kızamık (12-23 aylık çocuklara %'si)
22    Ölüm oranı, 5 yaş altı (her 1.000 canlı doğum ...
23    HIV yaygınlığı, toplam (15-49 yaş arası nüfusa...
24    Eğitime yapılan kamu harcaması, toplam (GSYİH ...
25               Okula kayıtlılık, ortaöğretim (brüt %)
26                Okula kayıtlılık, ilköğretim (brüt %)
27    İlköğretim bitirme oranı (ilgili yaş grubuna %...
28    İlk ve orta öğretimde kız öğrencilerin erkek ö...
29    Okuryazarlık oranı, toplam yetişkin (15 yaş ve...
35                   Kişi başına düşen GSYİH (cari USD)
36                              GSYİH büyüme (yıllık %)
37                                     GSYİH (cari USD)
38                Enflasyon, GSYİH deflatörü (yıllık %)
39                 Endüstri, katma değerli (GSYİH %'si)
40                    Tarım, katma değerli (GSYİH %'si)
41               Mal ve hizmet ithalatları (GSYİH %'si)
42        Gayri safi sabit sermaye oluşumu (GSYİH %'si)
43               Mal ve hizmet ihracatları (GSYİH %'si)
44                       Askeri harcamalar (GSYİH %'si)
45    Mobil cep telefonu abonelikleri (her 100 kişi ...
46                    İş kurmak için gereken süre (gün)
47    İş yapma kolaylığı endeksi (1=işletme dostu dü...
48                     Hibeler hariç gelir (GSYİH %'si)
49        Merkezi hükümet borçları, toplam (GSYİH %'si)
50     Araştırma ve geliştirme harcamaları (GSYİH %'si)
51             Enflasyon, tüketici fiyatları (yıllık %)
52    Yıllık temiz su çekilmeleri, toplam (iç kaynak...
53               CO2 emisyonları (kişi başı metrik ton)
54    Enerji kullanımı (kişi başı hampetrol kg eşdeğ...
55           Elektrik enerjisi tüketimi (kişi başı kWh)
56    Toplam borç servisi (mal, hizmet ihracı ve tem...
57      Alınan net resmi kalkınma yardımları (cari USD)
58    Dış borç stoku, toplam (DOD (devreden ödenmiş ...
59    Borsaya kayıtlı bir şirketin toplam hisse değe...
60                 Kişisel havaleler, alınan (cari USD)
61    Doğrudan yabancı yatırım, net girişler (BoP (ö...
62                                      Yüzölçümü (km2)
63                                    Orman alanı (km2)
64                Tarım arazisi (toprak parçasına %'si)
```
Pandas'da biraz daha ilerledikten sonra veri görselleştirmeye gireceğiz.

Sizlerden ricam bu verilerden istediğiniz bir şekilde görselleştirme yapmaya çalışın. Veri görselleştirme için seaborn kütüphanesini kullanabilirsiniz.

**Şurada örnekler var:**

https://seaborn.pydata.org/examples/index.html
Örneğin yıllara bağlı olarak orman alanlarının grafiğini çizdirebilirsiniz :slightly_smiling_face:

