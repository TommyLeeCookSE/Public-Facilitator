import sqlite3

# Connect to your database
conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')

with open('dump.sql', 'w') as f:
    for line in conn.iterdump():
        # Replace INSERT INTO with INSERT OR REPLACE INTO
        line = line.replace('INSERT INTO', 'INSERT OR REPLACE INTO')
        f.write('%s\n' % line)

# Close the connection
conn.close()

new_conn = sqlite3.connect('facilities_2.db')
c = new_conn.cursor()

# Then, read the dump file
with open('dump.sql', 'r') as f:
    sql = f.read()

# Execute the SQL commands to recreate the database
c.executescript(sql)

# Commit the changes and close the connection
new_conn.commit()
new_conn.close()