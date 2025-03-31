import mysql.connector

# Method 1 - Using MySQLCursor (Default)

# fetchall() returns a list of tuples.

cnx = mysql.connector.connect(user='root', password='mysqlroot',
                              host='127.0.0.1',
                              database='example_db')
cursor = cnx.cursor()
cursor.execute("select * from users;")

print("Method 1 output:")
for row in cursor.fetchall(): # Without `dictionary=True`.
    print(row)

cursor.close()
cnx.close()

# Method 2 - Using MySQLCursorDict

# fetchall() returns a list of dictionaries instead of tuples, allowing
# us to access data with the column name instead of the index.

cnx = mysql.connector.connect(user='root', password='mysqlroot',
                              host='127.0.0.1',
                              database='example_db')
cursor = cnx.cursor(dictionary=True) # With `dictionary=True`.
cursor.execute("select * from users;")

print("Method 2 output:")
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()
