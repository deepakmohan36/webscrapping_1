from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.3'
}
url = 'https://www.imdb.com/chart/top/'

try:
    source = requests.get(url, headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    
    movies = soup.find('ul',role='presentation').find_all('li',class_="ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent")

    for movie in movies:
        rank = movie.find('a',class_="ipc-title-link-wrapper").text.split('.')[0]
        name = movie.find('a',class_="ipc-title-link-wrapper").text.split('.')[1]

        
        meta_div = movie.find('div', class_='sc-14dd939d-5 cPiUKY cli-title-metadata')
        details = meta_div.find_all('span',class_='sc-14dd939d-6 kHVqMR cli-title-metadata-item')  

        year = details[0].text if len(details) > 0 else "N/A"
        rating = details[1].text if len(details) > 1 else "N/A"
        duration = details[2].text if len(details) > 2 else "N/A"

        score = movie.find('div', class_='sc-951b09b2-0 hDQwjv sc-14dd939d-2 fKPTOp cli-ratings-container').text[:3]
        
        print(f"Rank: {rank} Movie_Name:{name} Year_of_Release: {year} Rating: {rating} Duration: {duration} Imdb_Score: {score}")  

except Exception as e:
    print(e)

