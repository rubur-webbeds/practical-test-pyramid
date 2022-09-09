from databases import Database
import sqlite3
import os

db_name = "main.db"
database = Database(f"sqlite:///{db_name}")

async def connect():
    await database.connect()

async def remove_inmemory_db():
    os.remove(db_name)
    print("db deleted")

async def run_migration():
    sql_file = open("startup.sql", "r")
    startup_script = sql_file.read()
    sql_file.close()

    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.executescript(startup_script)
    con.commit()
    cur.close()
    con.close()
    print("db created")

async def fetch_user(last_name):
    query = "select first_name, last_name from users where last_name= :last_name"
    user = await database.fetch_one(query, values={"last_name": last_name})
    return user