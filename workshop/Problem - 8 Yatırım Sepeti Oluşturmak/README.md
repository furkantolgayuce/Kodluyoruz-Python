# Problem - 8: Yatırım Sepeti Oluşturmak

Pelin yapay zeka projeleri üreterek son 1 yıl içerisinde toplam 99 bin Türk Lirası para biriktirmeyi başarmıştır. Bu para ile yatırım yapmak istemektedir. 

Ekşi Sözlük'ten (https://eksisozluk.com/yatirim-sepeti--638320) "Yatırım Sepeti" diye bir şeyin olduğundan haberdar olmuştur. Bu yönteme göre yatırımların birden fazla araca birden yapılması durumunda riski aza indirebileceğini öğrenmiştir.

Elinde olan 99 bin Türk Lirasının,

*  3'te 1'ini çeyrek altın alarak

* 3'te 1'ini dolar alarak

*  3'te 1'ini de euro alarak değerlendirmek istemektedir. 

Fakat yatırım yapmak için acele etmek yerine bir hafta boyunca bu üç aracı (çeyrek altın, dolar, euro) gerçek zamanlı olarak takip eden bir programı Python ile yazmak istemektedir.

> Kodluyoruz Python Bootcamp'inde bunu Pandas ile aşağıdaki kod ile yapabilececeğini öğrenen Pelin işe koyulmuştur.

```
import pandas as pd
veriler = pd.read_html('http://finans.mynet.com/') 
```

Örneğin `veriler[11]` yaptığında altın fiyatlarını görebildiğini farketmiştir.

*SİZDEN İSTENENLER*

- Gerçek zamanlı olarak her bir dakikada bir Mynet Finans'tan Euro, Dolar ve çeyrek altın fiyatlarını çeken bir program yazınız.
- 1 saat boyunca çektiğiniz 60 veriyi bir Numpy dizisine yazınız.
- 99 bin lira ile kaç dolar kaç euro ve kaç çeyrek altın alınabileceğini her bir dakika için hesaplayın. 
