from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


def ferrobal_scrape_new(input):
    driver = input["driver"]

    driver.get(input["product"]["sku"])

    try:
        # price
        element = driver.find_element(By.NAME, "twitter:data1")
        price = element.get_attribute("content").replace(".", "").replace("$", "")
        price = int(price)
        # name
        element = driver.find_element(By.CLASS_NAME, "entry-title")
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
