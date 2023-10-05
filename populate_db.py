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

# Execute the query for question2
cursor.execute(schema_string2)

# Fetch the data
data = cursor.fetchall()


# Create an HTML table for question2
html2 = "<table>\n"
html2 += "<tr>\n"
html2 += "<th>column_1</th>\n"
html2 += "<th>column_2</th>\n"
html2 += "<th>column_3</th>\n"
html2 += "</tr>\n"
for row in data:
    html2 += "<tr>\n"
    html2 += "<td>{}</td>\n".format(row[0])
    html2 += "<td>{}</td>\n".format(row[1])
    html2 += "<td>{}</td>\n".format(row[2])
    html2 += "</tr>\n"
html2 += "</table>"


# Execute the query for question6
cursor.execute(schema_string6)

# Fetch the data
data = cursor.fetchall()

# Create an HTML table for question6
html6 = "<table>\n"
html6 += "<tr>\n"
html6 += "<th>column_1</th>\n"
html6 += "<th>column_2</th>\n"
html6 += "<th>column_3</th>\n"
html6 += "<th>column_4</th>\n"
html6 += "<th>column_5</th>\n"
html6 += "<th>column_6</th>\n"
html6 += "</tr>\n"
for row in data:
    html6 += "<tr>\n"
    html6 += "<td>{}</td>\n".format(row[0])
    html6 += "<td>{}</td>\n".format(row[1])
    html6 += "<td>{}</td>\n".format(row[2])
    html6 += "<td>{}</td>\n".format(row[3])
    html6 += "<td>{}</td>\n".format(row[4])
    html6 += "<td>{}</td>\n".format(row[5])
    html6 += "</tr>\n"
html6 += "</table>"


# Close the cursor and connection
cursor.close()
connection.close()

# Print the HTML table
print(html1)
print(html2)
print(html3)
print(html4)
print(html5)
print(html6)
