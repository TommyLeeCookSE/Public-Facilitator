import sqlite3

conn = sqlite3.connect(r'WebPages/facilities.db')
cursor = conn.cursor()

cursor.execute('''
               UPDATE walkin_tracker
               SET security = CASE
                    WHEN reason LIKE '%Badge%' THEN 1
                    ELSE 0
               END
               ''')


conn.commit()
conn.close()