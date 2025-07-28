from bs4 import BeautifulSoup

import requests


try:
    req=requests.get("https://helloomarket.com/")
    req.raise_for_status()  # Ensure we got a successful response
    soup=BeautifulSoup(req.text, 'html.parser')
    # print(soup.prettify)
    products=soup.find('div',class_='box-product').findAll('div',class_='product-items')
    print(len(products))
    for product in products:
        product_name = product.find('div', class_='product-details').a.text
        # price = product.find('span', class_='product-price').text.strip()
        print(product_name)
except Exception as e:
    print(f"An error occurred: {e}")