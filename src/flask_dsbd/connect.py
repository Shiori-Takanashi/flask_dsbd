import os

import psycopg
from dotenv import find_dotenv, load_dotenv


def connect() -> None:
    load_dotenv(find_dotenv(".env.local"))
    dbname = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    try:
        with psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        ):
            print("データベースへの接続が成功")
    except Exception as e:
        print(f"エラー発生: {e}")
