import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('dataset.db')
cur = conn.cursor()

# Create table AEC
cur.execute('''
CREATE TABLE IF NOT EXISTS AEC (
    Name TEXT,
    Specialization TEXT,
    HOD TEXT
)
''')

# Insert data into AEC table
cur.execute('''
INSERT INTO AEC (Name, Specialization, HOD) VALUES 
('Vikash Kumar Pandey', 'AIML', 'Dr Abhishek Bandyopadhyay'),
('Ishita Bej', 'IOT', 'Dr Debasis Chakraborty'),
('Arnab Chatterjee', 'AIML', 'Dr Abhishek Bandyopadhyay'),
('Shivam Mallick', 'CSBS', 'Dr Anup Kumar Mukhopadyay')
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
