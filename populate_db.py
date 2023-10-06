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
f2 = open("question2.sql", "r")
f6 = open("question6.sql", "r")
schema_string = f.read()
schema_string2 = f2.read()
schema_string6 = f6.read()

# Execute the query for question2
cursor.execute(schema_string2)

# Fetch the data
data = cursor.fetchall()


# Create an HTML table for question2
html2 = "<table>\n"
html2 += "<tr>\n"
html2 += "<th>Last Name</th>\n"
html2 += "<th>First Name</th>\n"
html2 += "<th>Absences</th>\n"
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
html6 += "<th>Last Name</th>\n"
html6 += "<th>First Name</th>\n"
html6 += "<th>Political Party</th>\n"
html6 += "<th>Number of Disagreements</th>\n"
html6 += "<th>Number of Agreements</th>\n"
html6 += "<th>Agreement Index</th>\n"
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
print(html2)
# print(html6)
