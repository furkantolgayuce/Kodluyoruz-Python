from bs4 import BeautifulSoup
import requests
import random
from TurkishStemmer import TurkishStemmer

r = requests.get('https://www.antoloji.com/siir/rastgele/')
source = BeautifulSoup(r.content,"html.parser")
siir = source.find("div", {"class":"pd-text"}).text

# Şiiri temizleyelim.
siir = siir.strip().lower()
siir = siir.replace("..."," ").replace("!"," ").replace(","," ").replace("("," ").replace(")"," ").replace("’"," ").replace("“"," ").replace("”"," ").replace("."," ").replace(","," ").replace("-"," ").replace(";"," ").replace(":"," ")
siir = siir.split()


# Köklerini bul.
stemmer = TurkishStemmer()
kok_liste = list()
for i in siir:
    kok = stemmer.stem(i)
    if len(kok) > 5 :
        kok_liste.append(kok)

# Yazar adı kaldır.
kok_liste = kok_liste[:-2]

# Rastgele kelime al.
random_kelime = random.randint(0,len(kok_liste))

kelime = kok_liste[random_kelime]

print(kelime)
