# flake8: noqa
import sys

sys.path.append("../")

from sqlalchemy.sql import text
from sqlalchemy import inspect
from utils.output import output_ERROR
from database import use_inventory_db, postgres_settings, engine


POSTGRES_HOST = postgres_settings.POSTGRES_HOST
POSTGRES_DB = postgres_settings.POSTGRES_DB
POSTGRES_PORT = postgres_settings.POSTGRES_PORT

IGNORE_TABLES = [
    "alembic_version",
    "External_persons",
    "Material_creations",
    "Permissions",
    "Price_details",
    "Product_materials",
    "Purchases",
    "Raw_material_repairs",
    "Register_product_details",
    "Register_tool_details",
    "Repair_details",
    "Repairs",
    "Role_permissions",
    "Sales",
    "Transaction_product_details",
    "Transaction_raw_material_details",
    "Transaction_tool_details",
    "User_creations",
    "User_permissions",
    "User_roles",
    "User_transactions",
    "Users",
]

# Configurar la conexión a la base de datos
print(
    f"Conectando a la base de datos {POSTGRES_DB} en"
    + f" {POSTGRES_HOST}:{POSTGRES_PORT}"
)
inspector = inspect(engine)


def get_tables_and_sequences():
    sequences = []
    for table in inspector.get_table_names():
        if table in IGNORE_TABLES:
            continue
        sequence = inspector.get_pk_constraint(table)
        if sequence and len(sequence["constrained_columns"]) == 1:
            sequences.append((table, sequence["constrained_columns"][0]))
    return sequences


def get_max_value(table, column):
    try:
        with use_inventory_db() as db:
            query = text(f'SELECT MAX("{column}") FROM "{table}"')
            result = db.execute(query).scalar()
            return result if result is not None else 0
    except Exception as e:
        output_ERROR(e, "get_max_value")
        return None


def get_sequence_idx(table_name, sequences):
    for sequence in sequences:
        if sequence.startswith(table_name):
            return sequence


def update_sequence_value():
    try:
        with use_inventory_db() as db:
            table_with_sequence = get_tables_and_sequences()
            sequences = inspector.get_sequence_names()
            for table, column in table_with_sequence:
                max_value = get_max_value(table, column)
                if max_value == 0:
                    continue
                sequence_name = get_sequence_idx(table, sequences)
                if not sequence_name:
                    continue
                init_sequence_value = max_value + 1
                query = text(
                    f'ALTER SEQUENCE public."{sequence_name}"'
                    + f"RESTART {init_sequence_value};"
                )
                db.execute(query)
                db.commit()
                print(
                    f"Secuencia ajustada para {table}.{column}."
                    + f" Nuevo valor: {init_sequence_value}"
                )

    except Exception as e:
        output_ERROR(e, "update_sequence_value")
        return e


update_sequence_value()
print("Ajuste de secuencias finalizado.")
