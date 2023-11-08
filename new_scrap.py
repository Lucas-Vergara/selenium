from mongo import connect_to_mongodb
from mongo import insert_or_update_product
from mongo import close_connection
from selenium import webdriver
from homecenter.homecenter_new import homecenter_scrape_new
from ferrobal.ferrobal_new import ferrobal_scrape_new
from yolito.yolito_new import yolito_scrape_new


def new_scrap(input):
    db = connect_to_mongodb("base_products")
    driver = webdriver.Chrome()
    products_collection = connect_to_mongodb("products")

    all_products = list(db.find())

    yolito_products = [
        product for product in all_products if product["distributor"] == "Yolito"
    ]
    sodimac_products = [
        product for product in all_products if product["distributor"] == "Sodimac (RM)"
    ]
    ferrobal_products = [
        product for product in all_products if product["distributor"] == "Ferrobal"
    ]

    driver.get("https://sodimac.falabella.com/sodimac-cl")
    for product in sodimac_products:
        scraped_product = homecenter_scrape_new(
            {"date": input["date"], "product": product, "driver": driver}
        )
        insert_or_update_product(products_collection, scraped_product)

    for product in ferrobal_products:
        scraped_product = ferrobal_scrape_new(
            {"date": input["date"], "product": product, "driver": driver}
        )
        insert_or_update_product(products_collection, scraped_product)

    base_url = "https://www.yolito.cl/Home/SetDeliveryMethod?isDelivery=True&idComuna="
    driver.get(base_url + "Las Condes")
    driver.get("https://www.yolito.cl/")
    for product in yolito_products:
        scraped_product = yolito_scrape_new(
            {"date": input["date"], "product": product, "driver": driver}
        )
        insert_or_update_product(products_collection, scraped_product)

    # Cerrar conexiones
    driver.quit()
    close_connection
