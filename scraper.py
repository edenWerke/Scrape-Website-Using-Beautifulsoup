from bs4 import BeautifulSoup

import requests


try:
    req=requests.get("https://zemenbazaar.com")
    req.raise_for_status()  # Ensure we got a successful response
    soup=BeautifulSoup(req.text, 'html.parser')
    print(soup)
except Exception as e:
    print(f"An error occurred: {e}")