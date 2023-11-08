from selenium import webdriver
from selenium.webdriver.common.by import By


def yolito_scrape_new(input):
    driver = input["driver"]

    base_product_url = "https://www.yolito.cl/Producto/"
    driver.get(base_product_url + input["product"]["sku"])

    try:
        # price
        element = driver.find_element(
            By.CSS_SELECTOR, 'span[style="font-size:30px;font-weight:bold"]'
        )
        price = element.text.replace(".", "").replace("$", "")
        price = int(price)
        # name
        element = driver.find_element(By.CSS_SELECTOR, ".s_info-name[itemprop='name']")
        web_title = element.text
        date = input["date"].strftime("%d-%m-%Y")

        product = {
            "datetime": input["date"],
            "date": date,
            "name": input["product"]["name"],
            "brand": input["product"]["brand"],
            "distributor": input["product"]["distributor"],
            "web_title": web_title,
            "sku": input["product"]["sku"],
            "presence": True,
            "price": price,
        }
        print(product)

    except:
        product = {
            "date": date,
            "name": input["product"]["name"],
            "brand": input["product"]["brand"],
            "distributor": input["product"]["distributor"],
            "web_title": None,
            "sku": input["product"]["sku"],
            "presence": False,
            "price": None,
        }
        print(product)

    return product
