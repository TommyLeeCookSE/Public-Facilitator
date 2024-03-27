company_dict = {
    "INFOSYS"                                       :   "INFOSYS LIMITED",
    "ROTH STAFFING COMPANIES, L.P. DBA ULTIMATE"    :   "ROTH STAFFING",
    "CONVERGINT TECHNOLOGIES LLC"                   :   "CONVERGINT",
    "PACIFIC BUILDING"                              :   "PACIFIC BUILDING CARE",
    "DELOITTE CONSULTING, LLP"                      :   "DELOITTE",
    "MBO PARTNERS, INC"                             :   "MBO PARTNERS",
    "CLUNE CONSTRUCTION COMPANY L.P"                :   "CLUNE CONSTRUCTION",
    "REDBOCK LLC"                                   :   "REDBOCK",
    "UNIVERSAL PROTECTION SERVICE, LP DBA"          :   "ALLIED UNIVERSAL",
    "MINDLANCE, LLC"                                :   "MINDLANCE, LLC",
    "BAXTER CREDIT UNION_UNITED STATES"             :   "BAXTER CREDIT UNION",
    "KELLY SERVICES PR_PUERTO RICO"                 :   "KELLY SERVICES",
    "MINDLANCE, LLC"                                :   "MINDLANCE"
    }

class Person:
    def __init__(self, fname, lname, EID, title, company, dept_num, supervisor_name,):
        self.fname              = fname
        self.lname              = lname
        self.EID                = EID
        self.title              = title
        self.company            = company
        self.dept_num           = dept_num
        self.supervisor_name    = supervisor_name
        self.location           = "IRVINE"
        self.clearance1         = "**GENERAL ACCESS - 24/7"
        self.clearance2         = "**GENERAL ACCESS (Varying Schedules)"
        self.clearance3         = "**LINC Access (0600-1800 M-F)"
        self.clearance4         = "**Parking Lot Access 24/7"

    def check_company_name(self):
        if self.company in company_dict:
            self.company = company_dict[self.company]


    def check_dept_num(self):
        self.dept_num = self.dept_num.lstrip('0123456789.- ')



def process(data):
    split = [line.upper().strip().split('\t') for line in data.split('\n')]
    employee_list = []
    for i,item in enumerate(split):
       employee_list.append(Person(split[i][0],split[i][1],split[i][2],split[i][3],split[i][4],split[i][5],split[i][6]))
    
    for i,item in enumerate(employee_list):
        employee_list[i].check_company_name()
        employee_list[i].check_dept_num()
    
    return employee_list