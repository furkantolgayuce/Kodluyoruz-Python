# Problem - 2

Şiirlerden Kelime Tahmini Oyunu

Bu program üç aşamadan oluşuyor.

- VERİNİN ÇEKİLMESİ: Herhangi bir şiir sitesinden bir şiirin Python ile çekilmesi (scrape etmek diye geçiyor)
- VERİNİN HAZIR HALE GETİRİLMESİ: Şiirde kelimelerden herhangi bir tanesini rastgele sayı üreterek seçmeniz ve bu kelimenin kökünü bulmanız
- OYUN: Kökü bulunan kelime ile kullanıcıya bir oyun oynatacaksınız. Bu hepimizin bildiği kelime tahmin oyunu.

OYUN KURALLARI
Tahmin edilmeye çalışılan kelime minimum 5 harften oluşmalıdır.
Kelimenin harf sayısının iki eksiği kadar kullanıcının hakkı olacak.

> Kelime sayısı n ise, kullanıcının hakkı (n-2) kadar olacak
> Kullanıcı her defasında bir harf alabilir.
> Her harf alınışında puan düşmektedir.
> Oyunun en başında puan sayısı harf sayısının iki katıdır.

Örnek olarak oyun şöyle ilerleyecek. "BALIK" kelimesi için

```
__,__,__,__,__ Puan: 10
__,A,__,__,__ Puan: 9
__,A,L,__,__ Puan: 8
__,A,L,__,K Puan: 7
_,A,L,I,K Puan: 6
```

Kullanılabilecek Araçlar:

**Verileri Çekmek için**
Scrapy: https://www.accordbox.com/blog/scrapy-tutorial-series-web-scraping-using-python/
beautifulsoup: http://omz-software.com/pythonista/docs/ios/beautifulsoup_guide.html

**Kelime Kökü Bulmak için**
Turkish Stemmer: https://github.com/otuncelli/turkish-stemmer-python
[Snowball-stemmer](https://medium.com/@aanilkayy/pythonda-snowball-stemmer-kullanılması-e91ed9be8e9e)