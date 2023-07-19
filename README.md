# IMDb Top 250 Movies Scraper

This is a simple Python script that scrapes the IMDb Top 250 movies list and displays relevant information about each movie. It uses the BeautifulSoup library to parse the HTML content of the IMDb webpage.

## Prerequisites

Before running the script, make sure you have the following installed:
- Python 3
- BeautifulSoup library (you can install it using `pip install beautifulsoup4`)
- Requests library (you can install it using `pip install requests`)

## How to Use

1. Clone the repository or download the `imdb_top_250_scraper.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `imdb_top_250_scraper.py` file.

3. Run the script by executing the following command:

```bash
python imdb_top_250_scraper.py
```

The script will start fetching the IMDb Top 250 movies data and display the following information for each movie:

- Rank: The movie's current position in the IMDb Top 250 list.
- Movie Name: The title of the movie.
- Year of Release: The year the movie was released.
- Rating: The movie's IMDb user rating.
- Duration: The duration of the movie.
- IMDb Score: The IMDb score of the movie.

## Note

- The script uses a custom User-Agent header to avoid blocking from IMDb. However, scraping websites may violate their terms of service, so use this script responsibly and considerate of IMDb's policies.

- If IMDb's website structure changes, the script may no longer work as expected. In that case, you might need to update the script accordingly.

- The script handles exceptions gracefully and prints error messages in case of any issues encountered during the scraping process.

## Disclaimer

This script is provided for educational and personal use only. The author is not responsible for any misuse or violation of IMDb's terms of service that may occur as a result of using this script.

Happy scraping and enjoy exploring the IMDb Top 250 movies list!
