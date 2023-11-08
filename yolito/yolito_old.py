from selenium import webdriver
from selenium.webdriver.common.by import By


def yolito_scrape_old(keys_list, comuna):
    driver = webdriver.Chrome()
    base_url = "https://www.yolito.cl/Home/SetDeliveryMethod?isDelivery=True&idComuna="
    driver.get(base_url + comuna)
    driver.get("https://www.yolito.cl/")

    products = []

    for key in keys_list:
        base_product_url = "https://www.yolito.cl/Producto/"
        driver.get(base_product_url + key[0])

        # Espera a que la página se cargue después de la búsqueda (puedes ajustar el tiempo según sea necesario)
        # driver.implicitly_wait(1)

        try:
            # price
            element = driver.find_element(
                By.CSS_SELECTOR, 'span[style="font-size:30px;font-weight:bold"]'
            )
            price = element.text
            # name
            element = driver.find_element(
                By.CSS_SELECTOR, ".s_info-name[itemprop='name']"
            )
            web_description = element.text
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
            product = {"SKU": key[0], "present": False, "precio": None}
            print(product)
            products.append(product)

    driver.quit()
    return products
