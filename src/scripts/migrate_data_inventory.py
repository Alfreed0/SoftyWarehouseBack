# flake8: noqa
import json
import os
import sys

sys.path.append("../")
from models import (
    Catalogue,
    Product,
    RawMaterial,
    Sector,
    Supplier,
    Tool,
    User,
    Permission,
    Transaction,
    InTransactionDetail,
    TransactionToolDetail,
    TransactionRawMaterialDetail,
    TransactionProductDetail,
    Purchase,
    PriceDetail
)
from database.db_inventory import use_inventory_db
from database.config import postgres_settings
from sqlalchemy.engine import URL

url = URL.create(
    drivername=postgres_settings.POSTGRES_DRIVER,
    username=postgres_settings.POSTGRES_USER,
    host=postgres_settings.POSTGRES_HOST,
    database=postgres_settings.POSTGRES_DB,
    password=postgres_settings.POSTGRES_PASSWORD,
    port=postgres_settings.POSTGRES_PORT,
)


file = "./data/"
json_files = os.listdir(file)

entities = {
    "Products": Product,
    "Sectors": Sector,
    "Users": User,
    "Catalogues": Catalogue,
    "RawMaterials": RawMaterial,
    "Suppliers": Supplier,
    "Tools": Tool,
    "Permissions": Permission,
    "Transactions": Transaction,
    "InTransactionDetails": InTransactionDetail,
    "TransactionToolDetails": TransactionToolDetail,
    "TransactionRawMaterialDetails": TransactionRawMaterialDetail,
    "TransactionProductDetails": TransactionProductDetail,
    "Purchases": Purchase,
    "PriceDetails": PriceDetail,
}

order_to_insert = [
    "Sectors",
    "Users",
    "Suppliers",
    "Catalogues",
    "RawMaterials",
    "Tools",
    "Products",
    "Permissions",
    "Transactions",
    "InTransactionDetails",
    "TransactionToolDetails",
    "TransactionRawMaterialDetails",
    "TransactionProductDetails",
    "Purchases",
    "PriceDetails",
]


def get_instances(json_obj):
    entity = entities[json_obj.get("tablename")]
    instances = [entity(**row) for row in json_obj.get("data")]
    return json_obj.get("tablename"), instances


# Iterar sobre los archivos JSON y cargarlos
dict_instances = {}
for json_f in json_files:
    ruta_completa = os.path.join(file, json_f)

    with open(ruta_completa) as archivo:
        datos = json.load(archivo)

    table, instances = get_instances(datos)
    dict_instances[table] = instances
with use_inventory_db() as db:
    for table in order_to_insert:
        db.add_all(dict_instances[table])
        db.commit()
        print(f"Se insertaron los datos de la tabla {table}")
