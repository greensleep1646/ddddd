import requests

def konum_bul(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        index = html_content.find('"geolocation"')
        if index != -1:
            start_index = html_content.find('"', index + len('"geolocation"') + 1) + 1
            end_index = html_content.find('"', start_index)
            konum = html_content[start_index:end_index]
            return konum
        else:
            return "Konum bilgisi bulunamadı."
    else:
        return "Kullanıcı bulunamadı veya bir hata oluştu."

username = input("TikTok kullanıcı adı: ")
konum = konum_bul(username)
print(f"{username} kullanıcısının konumu: {konum}")
