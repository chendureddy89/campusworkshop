"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqvs8u9tun42u51fm0-a.oregon-postgres.render.com",
        database="todo_task",
        user="todo_task_user",
        password="54GcXeu6NOZlpLLS6mFnuj6G4uI9Rez1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
