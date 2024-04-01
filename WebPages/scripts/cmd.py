import sqlite3

conn = sqlite3.connect(r'WebPages/facilities.db')
cursor = conn.cursor()


sql = "CREATE INDEX index_building_creation_date ON work_order_table (building, creation_date)"
cursor.execute(sql)

conn.commit()
conn.close()
