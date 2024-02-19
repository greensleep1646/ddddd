import requests
 
def konum_bul(kullanici_adi):
    url = f"https://www.tiktok.com/@{kullanici_adi}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_metni = response.text
        # Konumu alma işlemi burada yapılabilir, HTML içeriğini analiz ederek
        # Örnek olarak, "<meta property="og:location" content="New York, New York"/>" gibi bir öğeyi arayabilirsiniz.
        konum_baslangic_index = html_metni.find('<meta property="og:location" content="') + len('<meta property="og:location" content="')
        konum_bitis_index = html_metni.find('"', konum_baslangic_index)
        konum = html_metni[konum_baslangic_index:konum_bitis_index]
        return konum
    else:
        print("Hata! Sayfa yüklenirken bir sorun oluştu.")
        return None
 
# Kullanıcı adınızı belirterek konum bilgisini alabilirsiniz.
kullanici_adi = input("TikTok kullanıcı adını girin: ")
konum = konum_bul(kullanici_adi)
if konum:
    print(f"{kullanici_adi} kullanıcısının konumu: {konum}")
else:
    print("Konum bilgisi bulunamadı.")
