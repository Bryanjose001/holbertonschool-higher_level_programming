#!/usr/bin/python3
"""List all states in a database"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """connects to MySQL server"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or executing query: {e}")


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])