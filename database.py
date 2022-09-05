import sqlite3

#Queries
def CREATE_BEANS_TABLE():
    query = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
    return query

def INSERT_BEAN():
    query = "INSERT INTO beans (name, method, rating) VALUES (?,?,?);"
    return query

def GET_ALL_BEANS():
    query = "SELECT * FROM beans;"
    return query

def GET_BEANS_BY_NAME():
    query = "SELECT * FROM beans WHERE name = ?"
    return query

def GET_BEST_PREP_FOR_BEAN():
    query = """
    SELECT * FROM beans
    WHERE name = ?
    ORDER BY rating DESC
    LIMIT 1;
    """
    return query


def fetch_query(command):

    if command == "CREATE_BEANS_TABLE":
        return CREATE_BEANS_TABLE()
    elif command == "INSERT_BEAN":
        return INSERT_BEAN()
    elif command == "GET_ALL_BEANS":
        return GET_ALL_BEANS()
    elif command == "GET_BEANS_BY_NAME":
        return GET_BEANS_BY_NAME()
    elif command == "GET_BEST_PREP_FOR_BEAN":
        return GET_BEST_PREP_FOR_BEAN()

def connect():
    connection = sqlite3.connect("data.db")
    return connection

def create_tables(connection):
    with connection:
        connection.execute(fetch_query("CREATE_BEANS_TABLE"))

def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(fetch_query("INSERT_BEAN"), (name, method, rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(fetch_query("GET_ALL_BEANS")).fetchall()

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(fetch_query("GET_BEANS_BY_NAME"), (name,)).fetchall()

def get_best_prep_for_bean(connection, name):
    with connection:
        return connection.execute(fetch_query("GET_BEST_PREP_FOR_BEAN"),(name,)).fetchone()
