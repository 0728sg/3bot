import sqlite3
from db import queries

db= sqlite3.connect('db/store.sqlite')
cursor = db.cursor()


async def sql_create():
    if db:
        print("Data base is connected")

        cursor.execute(queries.CREATE_TABLE_PRODUCTS)
        cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)
        db.commit()

async def sql_insert_products(name_product, size, price, product_id, photo):
    with sqlite3.connect('db/store.sqlite') as db_with:
        cursor = db.cursor()
        cursor.execute(queries.INSERT_PRODUCTS_QUERY, (
            name_product,
            size,
            price,
            product_id,
            photo
        ))
        db_with.commit()
async def sql_insert_products_details(product_id, category, info_product):
    with sqlite3.connect('db/store.sqlite') as db_with:
        cursor = db.cursor()
        cursor.execute(queries.INSERT_PRODUCTS_QUERY_DETAILS, (
            product_id,
            category,
            info_product
        ))
        db_with.commit()