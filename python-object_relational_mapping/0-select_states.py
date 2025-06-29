#!/usr/bin/python3
"""This script connects to a MySQL database and lists all states"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """Connects to MySQL server and lists all states in ascending order by id"""
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            for state in cursor.fetchall():
                print(state)

        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or executing query: {e}")


if __name__ == "__main__":
    # Get command-line arguments and call the function
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
