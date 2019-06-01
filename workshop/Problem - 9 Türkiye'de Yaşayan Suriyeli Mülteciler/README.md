# Problem - 9 :Türkiye'de Yaşayan Suriyeli Mülteciler

Veri bilimcilerin amacı doğru bilgileri somut rakamlara dayanarak insanlara aktarmak ve çeşitli yöntemlerle bu rakamların anlaşılmasını sağlamaktır. https://multeciler.org.tr/turkiyedeki-suriyeli-sayisi/ adresinde Türkiye'ye göç eden Suriyeli insanlarla ilgili bazı sayısal bilgiler bulunmaktadır.

Amacımız bu sayfada yer iki tabloyu ("Yaş ve Cinsiyetlerine Göre Suriyelilerin Sayıları", "İllere Göre Suriyelilerin Sayısı") kullanarak tablolaların altında bulunan bilgileri elde etmek.

```
import pandas as pd
multeci = pd.read_html("https://multeciler.org.tr/turkiyedeki-suriyeli-sayisi/", header=0)
```

ile bu sayfadaki toplolara ulaşabiliriz. `multeci[0]` ilk tabloyu, `multeci[1]` ise ikinciyi tabloyu vermektedir.

İlk tablonun altında *Tabloya göre 0-18 yaş aralığında 1 milyon 662 bin 753 Suriyeli bulunuyor.* denilmektedir. Bu bilgiye tablodaki ilgili değerleri toplayarak ulaşabiliriz. Bu süreci Pandas ile yapabilirsek bu *rakamlar güncellendiğinde metni otomatik oluşturabiliriz*.

Bu değere ulaşmak için

```
pd.DataFrame(multeci[0]['TOPLAM'].loc[1:4]).astype(float).sum()
```

Yapmamız yeterli olacak.

https://multeciler.org.tr/turkiyedeki-suriyeli-sayisi/

*Sizden İstenenler*

Tablonun altında yer alan tüm açıklamaları tabloları ve Pandas'ı kullanarak elde edin. Görselleştirme yaparsanız da harika olur :slightly_smiling_face:
Bu raporu tablolar verildiğinde *otomatik olarak üreten* bir Python programı yazınız.