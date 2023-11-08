from selenium import webdriver
from selenium.webdriver.common.by import By


def homecenter_scrape_old(keys_list):
    driver = webdriver.Chrome()
    driver.get("https://sodimac.falabella.com/sodimac-cl")
    products = []

    for key in keys_list:
        barra_busqueda = driver.find_element(By.ID, "testId-SearchBar-Input")

        # Ingresa la clave en la barra de búsqueda
        barra_busqueda.clear()
        barra_busqueda.send_keys(key[0])

        # Haz clic en el botón de búsqueda
        driver.find_element(
            By.CLASS_NAME, "SearchBar-module_searchBtnIcon__2L2s0"
        ).click()

        try:
            # price
            element = driver.find_element(By.CSS_SELECTOR, "li[data-internet-price]")
            price = element.get_attribute("data-internet-price")
            # name
            element = driver.find_element(By.CSS_SELECTOR, "h1[data-name]")
            web_description = element.get_attribute("data-name")
            product = {
                "SKU": key[0],
                "presente": True,
                "precio": price,
                "descripcion_inicial": key[1],
                "descripcion_web": web_description,
            }
            print(product)
            products.append(product)
        except:
            product = {"SKU": key[0], "presente": False, "precio": None, "nombre": None}
            print(product)
            products.append(product)

    driver.quit()
    return products
