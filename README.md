# farm
animal Farm


#sözdekod #kabakod #algoritma

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
