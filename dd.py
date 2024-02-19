import requests

def get_tiktok_location(username):
    url = f'https://www.tiktok.com/@{username}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        # Bu kısımda HTML analizi yaparak konumu bulabilirsiniz.
        # TikTok'un web sitesindeki yapı değiştiğinde bu kodu güncellemelisiniz.
        # Örnek olarak, konumu "location" etiketinden alalım:
        location_index = html.find('"location"')
        if location_index != -1:
            start_index = html.find('"', location_index) + 1
            end_index = html.find('"', start_index)
            location = html[start_index:end_index]
            return location
        else:
            return "Konum bulunamadı."
    else:
        return "Sayfa yüklenirken bir hata oluştu."

# Kullanıcı adınızı girerek çalıştırın
username = input("TikTok kullanıcı adını girin: ")
location = get_tiktok_location(username)
print(f"{username} kullanıcısının konumu: {location}")
