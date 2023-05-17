"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7mim4dadc9vlunj6g-a.oregon-postgres.render.com",
        database="todo_5o3z",
        user="root",
        password="TDlHLcbRkEooDacpIUs3RQdZQwmEZaOH")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
