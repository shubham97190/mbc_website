import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='mbc_website_db',
    user="root",
    password="Abcd_1234")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * from auth_user")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()