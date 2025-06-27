#!/usr/bin/python3
"""This script connects to a MySQL database and lists all states"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """Connects to MySQL server and lists all states in ascending order by id"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or executing query: {e}")


if __name__ == "__main__":
    # Get command-line arguments and call the function
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])