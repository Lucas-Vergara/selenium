# mi_conexion.py

from pymongo import MongoClient


def connect_to_mongodb(collection):
    client = MongoClient(
        "mongodb+srv://lucasvergara1:pzk4zXVS0TPIWhZj@scrap.qyrybhz.mongodb.net/?retryWrites=true&w=majority"
    )
    db = client["test"]
    coleccion = db[collection]
    return coleccion


def insert_data(coleccion, datos):
    coleccion.insert_one(datos)


def close_connection(client):
    client.close()


def insert_or_update_product(collection, product):
    existing_product = collection.find_one(
        {
            "date": product["date"],
            "sku": product["sku"],
            "distributor": product["distributor"],
        }
    )

    if existing_product:
        update_query = {
            "date": product["date"],
            "sku": product["sku"],
            "distributor": product["distributor"],
        }
        update_operation = {"$set": product}
        collection.update_one(update_query, update_operation)
        print("Producto actualizado")
    else:
        collection.insert_one(product)
        print("Nuevo producto insertado")
