import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS biweekly_centerstone_report")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS biweekly_centerstone_report (
        date TEXT PRIMARY KEY,
        total_assigned_wo INTEGER,
        total_current_wo INTEGER,
        total_past_due_wo INTEGER,
        total_non_pm_wo INTEGER,
        total_current_non_pm_wo INTEGER,
        total_past_due_non_pm_wo INTEGER,
        total_pm_wo INTEGER,
        total_current_pm_wo INTEGER,
        total_past_due_pm_wo INTEGER,
        total_custodial_requests INTEGER,
        custodial_request_thirty_days INTEGER,
        custodial_request_seven_days INTEGER
    );
""")

conn.commit()
conn.close()
print("Completed")