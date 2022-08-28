import psycopg2
from config import host, password, db_name, user

try:
    ## connect to existing DB
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print('1')

    connection.autocommit = True  # Autocommit is on (it is not necessary to kommit DB)

    ## create cursor for operation with DB________________________
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    print('2')

    ## create a new table_____________________________________
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            nick_name VARCHAR(50) NOT NULL
            );
            """
        )
    print('Table created successfully')

    ## insert dats into a table ______________________________________________________
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users (first_name, nick_name) VALUES
            (
            'Oleg', 'Barracuda'
            );
            """
        )
    print('Data inserted successfully')


    ## Get data from Table _________________________________________________
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT nick_name FROM users WHERE first_name = 'Oleg';
            """
        )
        s = cursor.fetchone()
        print(s)

        ## DELETE DATA from Table _________________________________________________
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """
        #         DELETE FROM users WHERE first_name = 'Serg' ;
        #         """
        #     )
        #     print('Data "Serg" successfully deleted')


        ## DELETE Table _________________________________________________
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """
        #         DROP TABLE users ;
        #         """
        #     )
        #     print('Table "users" successfully deleted')


except Exception as _er:
    print('Error while working with PostgreSQL ', _er)

finally:
    if connection:
        connection.close
        print('PostgreSQL connection closed')
