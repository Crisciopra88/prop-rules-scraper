import requests
from bs4 import BeautifulSoup

url = "https://ftmo.com/it/faq/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

faq_elements = soup.find_all(["h2", "h3", "p", "li"])

with open("ftmo_faq.txt", "w") as file:
    for element in faq_elements:
        file.write(element.get_text(strip=True) + "\n")

print("✅ Estrazione completata: contenuto salvato in ftmo_faq.txt")
