from mylib.extract import extract
from mylib.query import create_db, read_db, update_db, delete_tb, Query1, Query2
from mylib.transform_load import load
import click
import sqlite3

@click.command()
@click.argument("db_file")
def main(db_file):
    conn=sqlite3.connect(db_file)
    print("Extracting data...")
    extract()

    print("Loading data...")
    load()

    print("Querying data...")
    create_db()
    print()
    read_db(conn)
    print()
    update_db(conn)
    print()
    delete_tb()
    print()
    load()
    print()
    Query1()
    print()
    Query2()
