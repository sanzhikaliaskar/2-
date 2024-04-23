import psycopg2
from config import host, user, password, db_name
import csv

try:
    #connect existing database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    #cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Select version: {cursor.fetchone()}")

    #create new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         first_name VARCHAR(50) NOT NULL,
    #         phone_number NUMERIC(11) NOT NULL);"""
    #     )
    #     print("[INFO] Table was succesfully created")
    
    
    #insert data into table
    '''with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, phone_number) VALUES ('John', '87777777777');"""
        )
        print("[INFO] Data succesfully inserted")
    '''

    #import data form csv 
    # with open('sample.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     next(reader)  # Skip the header row

    #     # Iterate over the rows in the CSV file and insert them into the database
    #     with connection.cursor() as cursor:
    #         for row in reader:
    #             cursor.execute(
    #                 "INSERT INTO users (first_name, phone_number) VALUES (%s, %s)",
    #                 (row[0], row[1])
    #             )
    #         print("[INFO] Data from csv file succesfully inserted")
    
    #updating information
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users SET first_name = 'Jonathan' WHERE id = 1;"""
    #     )
    #     print("[INFO] Data succesfully updated")
    

    #get data from table 
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT first_name, phone_number FROM users WHERE id = 2;"""
    #     )
    #     print(cursor.fetchone())
    
    

    #delete data from table
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM users WHERE id = 1;"""
        )
        print("[INFO] Data succesfully deleted")
    

    #delete whole table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users"""
    #     )
    #     print("[INFO] Table was succesfully deleted")
    

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
