import requests
from bs4 import BeautifulSoup

def scrape_ftmo():
    url = "https://ftmo.com/it/faq/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    text = soup.get_text(separator='\n')
    
    with open("ftmo.txt", "w") as f:
        f.write(text)

if __name__ == "__main__":
    scrape_ftmo()


add scraper.py
