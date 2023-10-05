import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    # user agent
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    # inserisci url della sitemap
    sitemap = input("Inserisci la Sitemap da scaricare: ")

    # invia la richiesta
    response = requests.get(sitemap)

    # cosa devo cercare (tutto sotto il formato di testo) / features="xml" è per visualizzare l'output su jupyter
    soup = BeautifulSoup(response.text, features="xml")

    # cosa devo estrarre
    links = [url.text for url in soup.find_all() if url.text.startswith("https://lookeronline.com")]

    # creo dizionario in Pandas per poi stampare il df
    data = {"Link":links}

    df = pd.DataFrame(data)

    df.to_csv("Sitemap_URL.csv", index = False)

    print("File salvato nella directory correttamente")
    
except Exception as e:
    print(f"Si è verificato un errore {e}")