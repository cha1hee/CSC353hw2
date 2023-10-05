import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    user='root',
    password='123456',
    host='localhost',
    database='SenateVotes'
)

# Get the cursor object
cursor = connection.cursor()
f = open("schema_and_data.sql", "r")
f1 = open("question1.sql", "r")
f2 = open("question2.sql", "r")
f3 = open("question3.sql", "r")
f4 = open("question4.sql", "r")
f5 = open("question5.sql", "r")
f6 = open("question6.sql", "r")
schema_string = f.read()
schema_string1 = f1.read()
schema_string2 = f2.read()
schema_string3 = f3.read()
schema_string4 = f4.read()
schema_string5 = f5.read()
schema_string6 = f6.read()

# Execute the query for question1
cursor.execute(schema_string1)

# Fetch the data
data = cursor.fetchall()

# Create an HTML table for question1
html = "<table>\n"
html += "<tr>\n"
html += "<th>column_1</th>\n"
html += "<th>column_2</th>\n"
html += "<th>column_3</th>\n"
html += "</tr>\n"
for row in data:
    html += "<tr>\n"
    html += "<td>{}</td>\n".format(row[0])
    html += "<td>{}</td>\n".format(row[1])
    html += "<td>{}</td>\n".format(row[2])
    html += "</tr>\n"
html += "</table>"

# Execute the query for question2
cursor.execute(schema_string2)

# Fetch the data
data = cursor.fetchall()

# Create an HTML table for question2
html = "<table>\n"
html += "<tr>\n"
html += "<th>column_1</th>\n"
html += "<th>column_2</th>\n"
html += "<th>column_3</th>\n"
html += "</tr>\n"
for row in data:
    html += "<tr>\n"
    html += "<td>{}</td>\n".format(row[0])
    html += "<td>{}</td>\n".format(row[1])
    html += "<td>{}</td>\n".format(row[2])
    html += "</tr>\n"
html += "</table>"

# Execute the query for question3
cursor.execute(schema_string1)

# Fetch the data
data = cursor.fetchall()

# Create an HTML table for question3
html = "<table>\n"
html += "<tr>\n"
html += "<th>column_1</th>\n"
html += "</tr>\n"
for row in data:
    html += "<tr>\n"
    html += "<td>{}</td>\n".format(row[0])
    html += "</tr>\n"
html += "</table>"

# Execute the query for question4
cursor.execute(schema_string1)

# Fetch the data
data = cursor.fetchall()

# Create an HTML table for question4
html = "<table>\n"
html += "<tr>\n"
html += "<th>column_1</th>\n"
html += "</tr>\n"
for row in data:
    html += "<tr>\n"
    html += "<td>{}</td>\n".format(row[0])
    html += "</tr>\n"
html += "</table>"


# Close the cursor and connection
cursor.close()
connection.close()

# Print the HTML table
print(html)
