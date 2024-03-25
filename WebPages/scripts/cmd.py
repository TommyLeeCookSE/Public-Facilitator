import sqlite3
print("running")
conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
connCursor = conn.cursor()
connCursor.execute("DELETE FROM daypasses WHERE card_number = ''")
conn.commit()
