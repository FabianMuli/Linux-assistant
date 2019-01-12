import sys
import wikipedia
import sqlite3

arguments = sys.argv

if len(arguments) >= 3:
    query = arguments[1] + " " + arguments[2]
else:
    query = arguments[1]


def search_database_whois(query, results):
    conn = sqlite3.connect('search.db')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM who_is WHERE Name = ?", (query,))
    data = cursor.fetchone()
    if data is None:
        conn.execute("INSERT INTO who_is (NAME, RESULTS) \
            VALUES (?,?)", [query, results])
        print("\n\nI have added " + query + " to my database.Results will be shown faster.")
    conn.commit()
    conn.close()


def check_database(query):
    conn = sqlite3.connect('search.db')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM who_is WHERE Name = ?", (query,))
    data = cursor.fetchone()
    if data is None:
        who_is()
    else:
        print(data[2])
    conn.commit()
    conn.close()


def who_is():
    try:
        results = wikipedia.summary(query)
        print(results)

        # save the results if they are not in the database
        search_database_whois(query, results)
    except:
        pass


check_database(query)
