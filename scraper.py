# from bs4 import BeautifulSoup
# from openpyxl import Workbook
# import requests

# def export_data(data):
#     excel=Workbook()
#     sheet=excel.active
#     sheet.title="Hello Market"
#     sheet.append(["Product Name", "Product Link", "Product Price"]) 
#     for item in data:
#         sheet.append([item['name'], item['link'], item['price']])
#     excel.save("hello_market_products.xlsx")
# try:
#     req=requests.get("https://helloomarket.com/")
#     req.raise_for_status()  # Ensure we got a successful response
#     soup=BeautifulSoup(req.text, 'html.parser')
#     # print(soup.prettify)
#     products=soup.find('div',class_='box-product').findAll('div',class_='product-items')
#     data=[]
#     print(len(products))
#     for product in products:
#         product_name = product.find('div', class_='product-details').a.text
#         product_link = product.find('div', class_='product-details').a.get('href')
#         product_price=product.find('div', class_='product-details').p.get_text(strip=True).split("Ex")[0].replace("ETB", "").strip()
    
#         data.append({
#             "name": product_name,
#             "link": product_link,
#             "price": product_price
#         })    
#         # price = product.find('span', class_='product-price').text.strip()
#         print(product_price)
# except Exception as e:
#     print(f"An error occurred: {e}")


from bs4 import BeautifulSoup
import requests, openpyxl

def export_data(data):
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "Helloo Market Data"
    # print(excel.sheetnames)
    sheet.append(['Product Name', 'Product Price', 'Product Link'])
    for item in data:
        sheet.append(item)
    excel.save(sheet.title+".xlsx")

try:
    req = requests.get("https://helloomarket.com/")
    req.raise_for_status()
    soup = BeautifulSoup(req.content, "html.parser")

    products = soup.find('div', class_="box-product").find_all('div', class_="product-items")
    data = []
    for product in products:
        product_name = product.find('div', class_="product-details").a.text
        product_link = product.find('div', class_="product-details").a.get("href")
        product_price = product.find('div', class_="product-details").p.get_text(strip=True).split("Ex")[0].replace("ETB", "")
        data.append([product_name,product_price, product_link])
        # break
    export_data(data)
except Exception as e:
    print(e)
    