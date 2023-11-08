from selenium import webdriver
from selenium.webdriver.common.by import By
from mongo import connect_to_mongodb


def homecenter_scrape_new(input):
    driver = input["driver"]

    # Ingresa la clave en la barra de búsqueda
    barra_busqueda = driver.find_element(By.ID, "testId-SearchBar-Input")
    barra_busqueda.clear()
    barra_busqueda.send_keys(input["product"]["sku"])

    # Haz clic en el botón de búsqueda
    driver.find_element(By.CLASS_NAME, "SearchBar-module_searchBtnIcon__2L2s0").click()

    try:
        # price
        element = driver.find_element(By.CSS_SELECTOR, "li[data-internet-price]")
        price = element.get_attribute("data-internet-price").replace(".", "")
        price = int(price)
        # name
        element = driver.find_element(By.CSS_SELECTOR, "h1[data-name]")
        web_title = element.get_attribute("data-name")

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
            "date": input["date"],
            "name": input["product"]["name"],
            "brand": input["product"]["brand"],
            "distributor": input["product"]["distributor"],
            "web_title": None,
            "sku": input["product"]["sku"],
            "presence": True,
            "price": None,
        }
        print(product)
    return product
