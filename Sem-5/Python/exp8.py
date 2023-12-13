import sqlite3

# Connect to the database
connection = sqlite3.connect("demo.db")
cursor = connection.cursor()

# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS Student")

# Create the Student table
table_query = """
CREATE TABLE Student (
    SAP_ID VARCHAR(255) NOT NULL,
    First_Name CHAR(25) NOT NULL,
    Last_Name CHAR(25),
    Address VARCHAR(255)
);
"""
cursor.execute(table_query)

# Insert data into the table
cursor.execute("""INSERT INTO Student VALUES ('120', 'Viraj', 'Das', 'Borivali')""")
cursor.execute("""INSERT INTO Student VALUES ('117', 'Dhruvi', 'Tank', 'Goregaon')""")
cursor.execute("""INSERT INTO Student VALUES ('115', 'Mihir', 'Vora', 'Kandivali')""")

# Print all data in the table
print("Data Inserted in the table:")
data = cursor.execute("""SELECT * FROM Student""")
for row in data:
    print(row)

# Select specific columns from the table
data2 = cursor.execute("""SELECT First_Name, Address FROM Student""")
for row in data2:
    print(row)

# Fetch one row from the result set
data3 = cursor.fetchone()
print(data3)

# Select data with a specific SAP_ID
data4 = cursor.execute('''SELECT * FROM Student WHERE SAP_ID="93"''')
for row in data4:
    print(row)

# Select data with Last_Name starting with 'G'
data5 = cursor.execute('''SELECT * FROM Student WHERE Last_Name LIKE "G%"''')
for row in data5:
    print(row)

# Delete data with SAP_ID "85"
cursor.execute('''DELETE FROM Student WHERE SAP_ID="85"''')

# Print the table after deletion
data6 = cursor.execute("""SELECT * FROM Student""")
for row in data6:
    print(row)

# Update Address where SAP_ID is '116'
cursor.execute("""UPDATE Student SET Address="Village" WHERE SAP_ID='115';""")
print(cursor.execute('''SELECT * FROM Student WHERE SAP_ID="115"'''))

# Add Email column to the table
cursor.execute("""ALTER TABLE Student ADD Email varchar(255);""")
cursor.execute(
    "INSERT INTO Student VALUES ('90', 'Husain', 'Rehmanji', 'Thane', 'gmail.com')"
)

# Select data for SAP_ID "90" after adding the Email column
data7 = cursor.execute('''SELECT * FROM Student WHERE SAP_ID="90" OR SAP_ID="115"''')
for row in data7:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
