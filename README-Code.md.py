# farm
animal Farm


#sözdekod #kabakod #algoritma #python

Problemi Tanımak:

Bir hayvanat bahçesi projesinde 500x500'lük bir alanda belirli sayıda hayvan yaşıyor. Her hayvanın belirli hareket kabiliyeti ve avlanma yetenekleri var. Bu hayvanlar arasında koyun, inek, tavuk, kurt, horoz ve aslanlar bulunuyor. Ayrıca bir avcı da bu alanda rasgele dolaşıyor ve belirli bir hareket kabiliyetine sahip. Her hayvanın belirli bir hareket kabiliyeti ve avlanma yetenekleri var. Belli bir hareket sonunda, hayvan sayılarının hesaplanması gerekiyor.

Kaba Kod:

plaintext
Copy code
Algoritma:
1. Hayvanların başlangıç konumlarını belirle.
2. Her adımda hayvanları rastgele hareket ettir.
3. Eğer kurt, tavuk, koyun veya horoz birbirine yakınsa, kurt avlar.
4. Eğer aslan inek veya koyuna yakınsa, avlanır.
5. Eğer avcı bir hayvana yakınsa, avlanır.
6. Her adımda, cinsiyetlerine ve yakınlıklarına göre yeni hayvanlar üret.
7. Belirli bir adımdan sonra, hayvan sayılarını hesapla ve ekrana yazdır.

Örnek Kaba Kod:
1. Hayvanların başlangıç konumlarını belirle.
2. Döngü başlat:
    - Her hayvanı rastgele bir yöne hareket ettir.
    - Eğer bir kurt, tavuk, koyun veya horoz birbirine yakınsa, kurt avlar.
    - Eğer bir aslan inek veya koyuna yakınsa, avlanır.
    - Eğer avcı bir hayvana yakınsa, avlanır.
    - Yeni hayvanlar üret.
    - Adım sayısını kontrol et, belirli bir adımdan sonra hayvan sayılarını hesapla.
3. Hayvan sayılarını ekrana yazdır.


import random
import math

class Hayvan:
    def __init__(self, x, y, cinsiyet):
        self.x = x
        self.y = y
        self.cinsiyet = cinsiyet

    def hareket_et(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def konum(self):
        return self.x, self.y

class Koyun(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

class Inek(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

class Tavuk(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

class Kurt(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

    def avla(self, diger_hayvan):
        mesafe = math.sqrt((self.x - diger_hayvan.x) ** 2 + (self.y - diger_hayvan.y) ** 2)
        if mesafe <= 4:
            return True
        return False

class Horoz(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

class Aslan(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

    def avla(self, diger_hayvan):
        mesafe = math.sqrt((self.x - diger_hayvan.x) ** 2 + (self.y - diger_hayvan.y) ** 2)
        if mesafe <= 5:
            return True
        return False

class Avcı(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)

    def avla(self, diger_hayvan):
        mesafe = math.sqrt((self.x - diger_hayvan.x) ** 2 + (self.y - diger_hayvan.y) ** 2)
        if mesafe <= 8:
            return True
        return False

def yeni_hayvan_uret(hayvanlar):
    for hayvan in hayvanlar:
        for diger_hayvan in hayvanlar:
            if hayvan is not diger_hayvan:
                if type(hayvan) == type(diger_hayvan) and hayvan.cinsiyet != diger_hayvan.cinsiyet:
                    mesafe = math.sqrt((hayvan.x - diger_hayvan.x) ** 2 + (hayvan.y - diger_hayvan.y) ** 2)
                    if mesafe <= 3:
                        yeni_cinsiyet = random.choice(['erkek', 'dişi'])
                        if isinstance(hayvan, Koyun):
                            hayvanlar.append(Koyun(hayvan.x, hayvan.y, yeni_cinsiyet))
                        elif isinstance(hayvan, Inek):
                            hayvanlar.append(Inek(hayvan.x, hayvan.y, yeni_cinsiyet))
                        elif isinstance(hayvan, Tavuk):
                            hayvanlar.append(Tavuk(hayvan.x, hayvan.y, yeni_cinsiyet))
                        elif isinstance(hayvan, Horoz):
                            hayvanlar.append(Horoz(hayvan.x, hayvan.y, yeni_cinsiyet))
                        elif isinstance(hayvan, Kurt):
                            hayvanlar.append(Kurt(hayvan.x, hayvan.y, yeni_cinsiyet))
                        elif isinstance(hayvan, Aslan):
                            hayvanlar.append(Aslan(hayvan.x, hayvan.y, yeni_cinsiyet))

def main():
    koyunlar = [Koyun(random.randint(0, 500), random.randint(0, 500), random.choice(['erkek', 'dişi'])) for _ in range(30)]
    inekler = [Inek(random.randint(0, 500), random.randint(0, 500), random.choice(['erkek', 'dişi'])) for _ in range(10)]
    tavuklar = [Tavuk(random.randint(0, 500), random.randint(0, 500), random.choice(['erkek', 'dişi'])) for _ in range(10)]
    kurtlar = [Kurt(random.randint(0, 500), random.randint(0, 500), random.choice(['erkek', 'dişi'])) for _ in range(10)]
    horozlar = [Horoz(random.randint(0, 500), random.randint(0, 500), random.choice(['erkek', 'dişi'])) for _ in range(10)]
    aslanlar = [Aslan(random.randint(0, 500), random.randint(0, 500), random.choice(['erkek', 'dişi'])) for _ in range(8)]
    avci = Avcı(random.randint(0, 500), random.randint(0, 500), 'avci')

  adim_sayisi = 1000
    for _ in range(adim_sayisi):
        for hayvan in koyunlar + inekler + tavuklar + kurtlar + horozlar + aslanlar + [avci]:
            hayvan.hareket_et()
        for kurt in kurtlar:
            for hayvan in koyunlar + tavuklar + horozlar:
                if kurt.avla(hayvan):
                    if hayvan in koyunlar:
                        koyunlar.remove(hayvan)
                    elif hayvan in tavuklar:
                        tavuklar.remove(hayvan)
                    elif hayvan in horozlar:
                        horozlar.remove(hayvan)
        for aslan in aslanlar:
            for hayvan in inekler + koyunlar:
                if aslan.avla(hayvan):
                    if hayvan in inekler:
                        inekler.remove(hayvan)
                    elif hayvan in koyunlar:
                        koyunlar.remove(hayvan)
        for hayvan in koyunlar + inekler + tavuklar + kurtlar + horozlar + aslanlar:
            if avci.avla(hayvan):
                if hayvan in koyunlar:
                    koyunlar.remove(hayvan)
                elif hayvan in inekler:
                    inekler.remove(hayvan)
                elif hayvan in tavuklar:
                    tavuklar.remove(hayvan)
                elif hayvan in kurtlar:
                    kurtlar.remove(hayvan)
                elif hayvan in horozlar:
                    horozlar.remove(hayvan)
                elif hayvan in aslanlar:
                    aslanlar.remove(hayvan)
        yeni_hayvan_uret(koyunlar + inekler + tavuklar + kurtlar + horozlar + aslanlar)
        if _ == adim_sayisi - 1:
            print("Son durum:")
            print(f"Koyun: {len(koyunlar)}")
            print(f"Inek: {len(inekler)}")
            print(f"Tavuk: {len(tavuklar)}")
            print(f"Kurt: {len(kurtlar)}")
            print(f"Horoz: {len(horozlar)}")
            print(f"Aslan: {len(aslanlar)}")

 if __name__ == "__main__":
       main()





