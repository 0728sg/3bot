import sqlite3
from db import queries

db= sqlite3.connect('db/store.sqlite')
cursor = db.cursor()


async def sql_create():
    if db:
        print("Data base is connected")

        cursor.execute(queries.CREATE_TABLE_PRODUCTS)
        db.commit()

    async def sql_insert_products(name_product, size, price, product_id, photo):
        cursor.execute(queries.INSERT_PRODUCTS_QUERY, (
            name_product,
            size,
            price,
            product_id,
            photo
        ))
        db.commit()