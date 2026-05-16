import psycopg2

host = "localhost"
port = "5432"
dbname = "recovery_app"
user = "postgres"
password = "cos101"

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )
            self.cursor = self.connection.cursor()
            print("Connection to PostgreSQL DB successful")
        except Exception as error:
            print(f"Error connecting to PostgreSQL DB: {error}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as error:
            print(f"Query error: {error}")
            self.connection.rollback()

    def fetch_one(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as error:
            print(f"Fetch error: {error}")
            return None

    def fetch_all(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as error:
            print(f"Fetch error: {error}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()