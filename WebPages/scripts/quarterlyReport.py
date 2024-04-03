import sqlite3
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


final_list = []

class Work_Order:
    def __init__(self, creation_date, is_pm, work_order_type, building):
        self.creation_date = creation_date
        self.is_pm = is_pm
        self.work_order_type = work_order_type
        self.building = building


class Quarterly_Report:
        def __init__(
                self, 
                date='',
                total_wo=0,
                total_pm=0,
                total_event=0,
                none=0,
                dbc_a=0,
                dbc_c=0,
                dbc_d=0,
                dbc_1=0,
                dbc_2=0,
                dbc_3=0,
                dbc_4=0,
                dbc_5=0,
                dbc_6=0,
                dbc_7=0,
                mic=0,
                workshop=0,
                prt=0,
                community=0,
                erc=0,
                linc=0,
                hvc=0,
                museum=0,
                lfs=0,
                lfsx=0,
                tnd=0,
                starr_atrium=0,
                mle=0,
                daimler_3009=0,
                daimler_17192=0,
                daimler_17152=0,
                ps1=0,
                ps2=0,
                ps3=0,
                alton_1901=0,
                alton_1902=0,
                duryea_1091=0,
                anton=0,
                kettering=0
                ):
            
                self.date = date
                self.total_wo = total_wo
                self.total_pm = total_pm
                self.total_event = total_event
                self.none = none
                self.dbc_a = dbc_a
                self.dbc_c = dbc_c
                self.dbc_d = dbc_d
                self.dbc_1 = dbc_1
                self.dbc_2 = dbc_2
                self.dbc_3 = dbc_3
                self.dbc_4 = dbc_4
                self.dbc_5 = dbc_5
                self.dbc_6 = dbc_6
                self.dbc_7 = dbc_7
                self.mic = mic
                self.workshop = workshop
                self.prt = prt
                self.community = community
                self.erc = erc
                self.linc = linc
                self.hvc = hvc
                self.museum = museum
                self.lfs = lfs
                self.lfsx = lfsx
                self.tnd = tnd
                self.starr_atrium = starr_atrium
                self.mle = mle
                self.daimler_3009 = daimler_3009
                self.daimler_17192 = daimler_17192
                self.daimler_17152 = daimler_17152
                self.ps1 = ps1
                self.ps2 = ps2
                self.ps3 = ps3
                self.alton_1901 = alton_1901
                self.alton_1902 = alton_1902
                self.duryea_1091 = duryea_1091
                self.anton = anton
                self.kettering = kettering

building_to_attr = {
    "1091 Duryea - Warehouse": "duryea_1091",
    "17152 Daimler": "daimler_17152",
    "17192 Daimler - Warehouse": "daimler_17192",
    "1821 Kettering": "kettering",
    "1901 Alton": "alton_1901",
    "1921 Alton": "alton_1902",
    "3009 Daimler": "daimler_3009",
    "535 Anton": "anton",
    "Community Center": "community",
    "DBC Building A": "dbc_a",
    "DBC Building C": "dbc_c",
    "DBC Building D": "dbc_d",
    "DBC Pod 1": "dbc_1",
    "DBC Pod 2": "dbc_2",
    "DBC Pod 3": "dbc_3",
    "DBC Pod 4": "dbc_4",
    "DBC Pod 5": "dbc_5",
    "DBC Pod 6": "dbc_6",
    "DBC Pod 7": "dbc_7",
    "Edwards Research Center": "erc",
    "Founders Workshop Pavilion": "workshop",
    "Heart Valve Center": "hvc",
    "Lifesciences": "lfs",
    "Lifesciences Extension": "lfsx",
    "LINC": "linc",
    "MLE": "mle",
    "Mussallem Innovation Center": "mic",
    "Parking Structure 1": "ps1",
    "Parking Structure 2": "ps2",
    "Parking Structure 3": "ps3",
    "Partners": "prt",
    "Starr Atrium": "starr_atrium",
    "T&D": "tnd",
    "The Museum": "museum",
    None: "none"
}

def queryDatabase(date1, date2):
    start_date = datetime.strptime(date1,'%Y-%m-%d')
    end_date = datetime.strptime(date2,'%Y-%m-%d')
    month_1 = start_date
    month_2 = start_date + relativedelta(months = 1) 
    month_3 = start_date + relativedelta(months = 2) 

    start_date_prev_year    =     start_date.replace(year = start_date.year - 1)
    end_date_prev_year      =     end_date.replace(year = end_date.year -1)
    month_1_prev_year       =     start_date_prev_year
    month_2_prev_year       =     month_2.replace(year = month_2.year - 1)
    month_3_prev_year       =     month_3.replace(year = month_3.year - 1)

    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    month_1=month_1.strftime('%Y-%m-%d')
    month_2=month_2.strftime('%Y-%m-%d')
    month_3=month_3.strftime('%Y-%m-%d')

    start_date_prev_year=start_date_prev_year.strftime('%Y-%m-%d')
    end_date_prev_year=end_date_prev_year.strftime('%Y-%m-%d')
    month_1_prev_year=month_1_prev_year.strftime('%Y-%m-%d')
    month_2_prev_year=month_2_prev_year.strftime('%Y-%m-%d')
    month_3_prev_year=month_3_prev_year.strftime('%Y-%m-%d')
    


    with sqlite3.connect(r'WebPages/facilities.db') as conn:
        cursor = conn.cursor()
        #Need to use a forloop here instead, iterate through all the dates which will be in a list
        cursor.execute("SELECT creation_date, is_pm, work_order_type, building FROM work_order_table WHERE creation_date > ? AND creation_date < ?", (start_date, end_date))
        result = cursor.fetchall()

        process_query_data(result)
        
        

def process_query_data(result):
    temp_list = []
    quarterly_report_object = Quarterly_Report()

    for row in result:
        temp_list.append(Work_Order(*row))
        
    
    for workorder in temp_list:
        #need to figure out how t get the right date, probably pass in date and use that
        quarterly_report_object.total_wo += 1
        if workorder.is_pm == "1":
            quarterly_report_object.total_pm +=1
        if "Meeting Request -" in workorder.work_order_type:
            quarterly_report_object.total_event +=1
        if workorder.building in building_to_attr:
             attr_name = building_to_attr[workorder.building]
             if hasattr(quarterly_report_object, attr_name):
                  current_value = getattr(quarterly_report_object, attr_name)
                  setattr(quarterly_report_object, attr_name, current_value +1)


    # print(vars(quarterly_report_object))

    final_list.append(quarterly_report_object)
#Return final_list
         


queryDatabase('2024-01-01', '2024-03-31')