import os, sqlite3, datetime

def process():
        conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
        cursor = conn.cursor()

        totalWO = totalNonPM = totalPM = totalCurrentWO = totalCurrentPM = totalPastDueWO = custodialRequestCounter = custodial30days = custodial7days = totalCurrentNonPM = totalPastNonPM = totalCurrentPM = totalPastPM = 0
        today = datetime.date.today()

        #Total Wo Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*'")
        totalWO = cursor.fetchone()[0]
        print(f'Total Assigned Work Orders: {totalWO}')

        #Total Current WO Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND completion_due >= ?",(today,))
        totalCurrentWO = cursor.fetchone()[0]
        print(f'Total Current WO: {totalCurrentWO}')

        #Total Past Due WO Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND completion_due < ?",(today,))
        totalPastDueWO = cursor.fetchone()[0]
        print(f'Total Past Due WO: {totalPastDueWO}')
        print()

        #Total Non PM Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND is_pm = 0")
        totalNonPM = cursor.fetchone()[0]
        print(f'Total Non PM Work Order: {totalNonPM}')

        #Total Current Non PM Counter 
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND is_pm = 0 AND completion_due >= ?",(today,))
        totalCurrentNonPM = cursor.fetchone()[0]
        print(f'Total Current Non PM Work Order: {totalCurrentNonPM}')

        #Total Past Due Non PM Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND is_pm = 0 AND completion_due < ?",(today,))
        totalPastNonPM = cursor.fetchone()[0]
        print(f'Total Past Due Non PM Work Order: {totalPastNonPM}')
        print()


        #Total PM WO Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND is_pm = 1")
        totalPM = cursor.fetchone()[0]
        print(f'Total PM Work Order: {totalPM}')

        #Total Current PM Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND is_pm = 1 AND completion_due >= ?",(today,))
        totalCurrentPM = cursor.fetchone()[0]
        print(f'Total Current PM: {totalCurrentPM}')

        #Total Past Due PM Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE status LIKE 'Assigned*' AND is_pm = 0 AND completion_due < ?",(today,))
        totalPastPM = cursor.fetchone()[0]
        print(f'Total Past Due PM Work Order: {totalPastPM}')
        print()
        print()

        #Total Custodial Request Counter
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE work_order_type LIKE 'Custodial Request%'")
        custodialRequestCounter = cursor.fetchone()[0]
        print(f'Total Custodial Work Order: {custodialRequestCounter}')

        #Total Custodial Request 30 days Counter
        thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE work_order_type LIKE 'Custodial Request%' AND creation_date >= ?", (thirty_days_ago,))
        custodial30days = cursor.fetchone()[0]
        print(f'Total Custodial 30 days Work Order: {custodial30days}')

        #Total Custodial Request 7 days Counter
        seven_days_ago = datetime.date.today() - datetime.timedelta(days=7)
        cursor.execute("SELECT COUNT(*) FROM work_order_table WHERE work_order_type LIKE 'Custodial Request%' AND creation_date >= ?", (seven_days_ago,))
        custodial7days = cursor.fetchone()[0]
        print(f'Total Custodial 7 days Work Order: {custodial7days}')
        
        
        query = '''
        INSERT OR REPLACE INTO biweekly_centerstone_report
        (date, total_assigned_wo, total_current_wo, total_past_due_wo,total_non_pm_wo,total_current_non_pm_wo,total_past_due_non_pm_wo,total_pm_wo,total_current_pm_wo,total_past_due_pm_wo,total_custodial_requests,custodial_request_thirty_days, custodial_request_seven_days)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

        parameters = (today, totalWO,totalCurrentWO,totalPastDueWO,totalNonPM,totalCurrentNonPM,totalPastNonPM,totalPM,totalCurrentPM,totalPastPM,custodialRequestCounter,custodial30days,custodial7days)

        cursor.execute(query, parameters)

        conn.commit()
        conn.close()
        return [today,totalWO,totalCurrentWO,totalPastDueWO,custodialRequestCounter,totalNonPM,totalCurrentNonPM,totalPastNonPM,totalPM,totalCurrentPM,totalPastPM,custodial7days,custodial30days]



