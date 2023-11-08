# main.py

from homecenter.homecenter_old import homecenter_scrape_old
from yolito.yolito_old import yolito_scrape_old
from ferrobal.ferrobal_old import ferrobal_scrape_old
from mongo import connect_to_mongodb
from mongo import insert_data
from mongo import close_connection
from datetime import datetime


def old_scrap():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    homecenter_data = homecenter_scrape_old(
        [
            ["110282078", "Yeso Saco 25 kg Romeral"],
            ["110322665", "Yeso Saco 25 kg Volcán"],
            ["110303531", "Yeso Cartón ST 10 mm Volcán"],
        ],
    )
    yolito_data = yolito_scrape_old(
        [
            ["2910006685225", "Yeso Saco 25 kg Romeral"],
            ["1219040710346", "Yeso Cartón ST 10 mm Knauf"],
            ["2910006686697", "Yeso Saco 25 kg Volcán"],
        ],
        "LAS CONDES",
    )
    ferrobal_data = ferrobal_scrape_old(
        [
            [
                "https://ferrobal.cl/producto/yeso-espuma-romeral-25kg/",
                "Yeso Saco 25 kg Romeral",
            ],
            [
                "https://ferrobal.cl/producto/masilla-base-romeral-25-kg/",
                "Masilla Base 25 kg Gyplac",
            ],
            [
                "https://ferrobal.cl/producto/volcanita-rh-15mm-12x24m/",
                "Yeso Cartón RH 15 mm Volcán",
            ],
        ]
    )

    scrap = {
        "date": date,
        "homecenter": homecenter_data,
        "yolito": yolito_data,
        "ferrobal": ferrobal_data,
    }
    # Conexión a MongoDB
    db = connect_to_mongodb("scrapData")

    # Almacenar datos en MongoDB
    insert_data(db, scrap)

    # Cerrar conexiones
    close_connection
