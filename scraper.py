import requests
from bs4 import BeautifulSoup

def estrai_testo_ftmo():
    url = "https://ftmo.com/it/faq/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    blocchi = soup.find_all(['h1', 'h2', 'h3', 'p', 'li'])
    testo = "\n".join([b.get_text(strip=True) for b in blocchi])

    with open("ftmo_faq.txt", "w", encoding="utf-8") as f:
        f.write(testo)

    print("✅ Estrazione completata: contenuto salvato in ftmo_faq.txt")

if __name__ == "__main__":
    estrai_testo_ftmo()
