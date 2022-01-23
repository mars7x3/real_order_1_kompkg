
import time

from datetime import datetime
from decimal import Decimal as D
from peewee import *
from parsing_store import main
from decouple import config



def mysql_connect():
    mysql_db = MySQLDatabase(config('my_base'), 
                        user=config('my_user'), 
                        password=config('my_password'), 
                        host=config('my_host'), 
                        port=3306)
    return mysql_db


def update_price_in_db(price, id):
    if price < D(500):
        mysql_connect().execute_sql(f"UPDATE komp_product_prices SET price = {price - D(5)} WHERE product_id = {id}")
    elif price > D(500) and price < D(5000):
        mysql_connect().execute_sql(f"UPDATE komp_product_prices SET price = {price - D(10)} WHERE product_id = {id}")
    else:
        mysql_connect().execute_sql(f"UPDATE komp_product_prices SET price = {price - D(20)} WHERE product_id = {id}")


def chek_price():
    start_time = datetime.now()
    mysql_db_columns = mysql_connect().execute_sql("select p.product_id, p.product_code, kp.price from komp_products as p \
                                            join komp_product_prices as kp where kp.product_id = p.product_id",)
    counter = 0
    for product_id, product_article, product_price  in mysql_db_columns:
        counter += 1        
        if counter == 1000: time.sleep(5)
        store_price = main(product_article)
        if store_price and store_price != D(product_price):
            update_price_in_db(store_price, product_id)

    finish_time = datetime.now()
    return str(finish_time - start_time)[:-7]
        


