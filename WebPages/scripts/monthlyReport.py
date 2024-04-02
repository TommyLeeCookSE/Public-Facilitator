import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta

final_list = []

def queryDatabase(
        start_date_current, end_date_current,
        first_month_current, second_month_current, third_month_current,
        stard_date_previous, end_date_previous,
        first_month_previous, second_month_previous, third_month_previous):


    with sqlite3.connect(r'WebPages/facilities.db') as conn:
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (start_date_current, end_date_current))
        result = cursor.fetchall()
        process_query_data(result)

        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (first_month_current, second_month_current))
        result = cursor.fetchall()
        process_query_data(result)

        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (second_month_current, third_month_current))
        result = cursor.fetchall()
        process_query_data(result)

        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (third_month_current, end_date_current))
        result = cursor.fetchall()
        process_query_data(result)



        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (stard_date_previous, end_date_previous))
        result = cursor.fetchall()
        process_query_data(result)

        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (first_month_previous, second_month_previous))
        result = cursor.fetchall()
        process_query_data(result)

        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (second_month_previous, third_month_previous))
        result = cursor.fetchall()
        process_query_data(result)

        cursor.execute("SELECT * FROM work_order_table WHERE creation_date > ? AND creation_date < ?",
                       (third_month_previous, end_date_previous))
        result = cursor.fetchall()
        process_query_data(result)
        
        

def process_query_data(result):
        total_wo = 0
        total_pm = 0
        total_events = 0
        wo_per_building = {}
        wo_per_category = {}
        temp_list = []


        for row in result:
            total_wo += 1
            wo_per_building[row[6]] = wo_per_building.get(row[6],0) + 1
            wo_per_category[row[9]] = wo_per_category.get(row[9],0) + 1
            if row[10] == "1":
                total_pm += 1
            if "Meeting Request" in row[9]:
                total_events += 1

            
        for key,value in wo_per_building.items():
            # print(f"{key}:\t{value}")
            temp_list.append([key,value])

        for key,value in wo_per_category.items():
            if "Electrical -" in key:
                # print(f"{key}\t{value}")
                temp_list.append([key,value])
            elif "Plumbing -" in key:
                # print(f"{key}\t{value}")
                temp_list.append([key,value])
            elif "Misc." in key:
                # print(f"{key}\t{value}")
                temp_list.append([key,value])

        # print(f"Total WO:\t{total_wo}")
        temp_list.append(["Total WO:",total_wo])
        # print(f"Total PM:\t{total_pm}")
        temp_list.append(["Total PM:",total_pm])
        # print(f"Total Events:\t\t{total_events}")
        temp_list.append(["Total Events:",total_events])
        # print(f"Total Moves:\t")
        final_list.append(temp_list)



queryDatabase('2024-01-01','2024-03-31',
              '2024-01-01','2024-02-01','2024-03-01',
              '2023-01-01','2023-03-31',
              '2023-01-01','2023-02-01','2023-03-01')

print(final_list[0])