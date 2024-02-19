import requests

def find_location(username):
    url = f'https://www.tiktok.com/@{username}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = response.text
        # Assuming the location is in the HTML, you might need to parse it accordingly.
        # Bu örnekte TikTok'un sitesinden veri çekmek için bir scraper kullanıyoruz.
        # Daha sofistike bir uygulama için TikTok API'sini kullanabilirsiniz.
        # HTML içeriğinden konumu aramak için uygun bir analiz yapmalısınız.
        # Örneğin, BeautifulSoup gibi bir kütüphane kullanabilirsiniz.
        location_index = html.find('"geolocation":') + len('"geolocation":')
        location_start_index = html.find('"', location_index) + 1
        location_end_index = html.find('"', location_start_index)
        location = html[location_start_index:location_end_index]
        return location
    else:
        return None

# Kullanıcı adını belirtin
username = 'kullanıcı_adı'
location = find_location(username)
if location:
    print(f"{username}'un konumu: {location}")
else:
    print("Konum bulunamadı.")
