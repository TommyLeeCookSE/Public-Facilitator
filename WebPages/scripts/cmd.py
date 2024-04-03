import sqlite3

conn = sqlite3.connect(r'WebPages/facilities.db')
cursor = conn.cursor()


sql = "CREATE INDEX index_creation_date ON work_order_table (creation_date)"
cursor.execute(sql)

conn.commit()
conn.close()
