from selenium import webdriver
from selenium.webdriver.common.by import By


def ferrobal_scrape_old(url_list):
    driver = webdriver.Chrome()
    products = []

    for url in url_list:
        driver.get(url[0])

        # Espera a que la página se cargue después de la búsqueda (puedes ajustar el tiempo según sea necesario)
        # driver.implicitly_wait(1)

        try:
            # price
            element = driver.find_element(By.NAME, "twitter:data1")
            price = element.get_attribute("content")
            # name
            element = driver.find_element(By.CLASS_NAME, "entry-title")
            web_description = element.text
            product = {
                "SKU": url[0],
                "presente": True,
                "precio": price,
                "descripcion_inicial": url[1],
                "descripcion_web": web_description,
            }
            print(product)
            products.append(product)

        except:
            product = {"SKU": url[0], "present": False, "precio": None}
            print(product)
            products.append(product)

    driver.quit()
    return products
