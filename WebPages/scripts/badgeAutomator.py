import re

company_dict = {
    r'.*INFOSYS.*'             :"INFOSYS",
    r'.*INFOSOFT.*'            :"INFOSOFT",
    r'.*GRANT THORNTON.*'      :"GRANT THORNTON",
    r'.*ROTH.*'                :"ROTH STAFFING",
    r'.*CONVERGINT.*'          :"CONVERGINT",
    r'.*PACIFIC BUILDING.*'    :"PACIFIC BUILDING CARE",
    r'.*DELOITTE.*'            :"DELOITTE",
    r'.*MBO.*'                 :"MBO PARTNERS",
    r'.*CLUNE.*'               :"CLUNE CONSTRUCTION",
    r'.*REDBOCK.*'             :"REDBOCK",
    r'.*UNIVERSAL.*SERVICE.*'  :"ALLIED UNIVERSAL",
    r'.*MINDLANCE.*'           :"MINDLANCE",
    r'.*BAXTER.*'              :"BAXTER CREDIT UNION",
    r'.*BCU.*'                 :"BAXTER CREDIT UNION",
    r'.*KELLY SERVICES.*'      :"KELLY SERVICES",
    r'.*IST.*'                 :"IST MANAGEMENT",
    r'.*THE CLEANNERS.*'       :"THE CLEANERS",
    r'.*PRIVATE CAR WASH.*'    :"PRIVATE CAR WASH",
    r'.*MAGNIT.*'              :"MAGNIT",
    r'.*PLANET PHARMA.*'       :"PLANET PHARMA",
    r'.*BON APPETIT.*'         :"BON APPETIT",
    r'.*360 TALENT SOLUTIONS.*':"360 TALENT SOLUTIONS",
    r'.*VWR.*'                 :"VWR",
    r'.*COAST PACIFIC.*'       :"COAST PACIFIC BUILDERS",
    r'.*9EDGE.*'               :"9 EDGE",
    r'.*TALENTBURST.*'         :"TALENTBURST",
    r'.*BEACON HILL.*'         :"BEACON HILL STAFFING GROUP",
    r'.*PWC.*'                 :"PWC",
    r'.*J\.A.*'                 :"J.A. STOWELL",
    r'.*TANGRAM.*'             :"TANGRAM",
    r'.*COMPUNNEL.*'           :"COMPUNNEL SOFTWARE GROUP",
    r'.*FOCUS MARKETING.*'     :"FOCUS MARKETING",
    r'.*THE ANTI.*'            :"THE ANTI",
    r'.*MINITAB.*'             :"MINITAB",
    r'.*SKADDEN.*'             :"SKADDEN ARPS SLATE MEAGHER & FLOM LLP",
    r'.*PROCRAFT.*'            :"PROCRAFT MEDIA",
    r'.*SPINITAR.*'            :"SPINITAR",
    r'.*SYSAZZLE.*'            :"SYSAZZLE",
    r'.*HYDROGEN PROF.*'       :"HYDROGEN PROFESSIONAL SERVICES",
    r'.*LINQM.*'               :"LINQM",
    r'.*ACTALENT.*'            :"ACTALENT",
    r'.*RADIANT SYS.*'         :"RADIANT SYSTEMS",
    r'.*IRON MOUNTAIN.*'       :"IRON MOUNTAIN",
    r'.*NEWPORT WINDOW.*'      :"NEWPORT WINDOW MAINTENANCE",
    r'.*ALIGN B.*'             :"ALIGN BUILDERS",
    r'.*INTELLECTT.*'          :"INTELLECTT",
    r'.*QUALITY DUAL.*'        :"QUALITY DUAL INTEGRA SL",
    r'.*EMCOR.*'               :"EMCOR",
    r'.*NAVIEN.*'              :"NAVIEN",
    }

company_clearance_dict = {
    "ALLIED UNIVERSAL"     :"IRV_Security Guards",
    "BON APPETIT"          :"IRV_Bon Appetit General Access - New Cafe, LINC and MLE Atrium -J.Alberga",
    "PACIFIC BUILDING CARE":"IRV_Janitorial Access"
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
        self.clearance_list = ["**GENERAL ACCESS - 24/7","**GENERAL ACCESS (Varying Schedules)","**LINC Access (0600-1800 M-F)","**Parking Lot Access 24/7"]

    def check_company_name(self):
        self.company = self.company.strip()
        for pattern, replacement in company_dict.items():
            if re.match(pattern, self.company, flags=re.IGNORECASE):
                self.company = replacement
                break

    def add_clearance(self,clearance):
            self.clearance_list.append(clearance)

    def check_clearances(self):
        if self.company in company_clearance_dict:
            self.add_clearance(company_clearance_dict[self.company])

    def check_dept_num(self):
        self.dept_num = self.dept_num.lstrip('0123456789.- ')
    
    
        

def process(data):
    split = [line.upper().strip().split('\t') for line in data.split('\n')]
    employee_list = []
    for i,item in enumerate(split):
       employee_list.append(Person(split[i][0].strip(),split[i][1].strip(),split[i][2].strip(),split[i][3].strip(),split[i][4].strip(),split[i][5].strip(),split[i][6].strip()))
    
    for i,item in enumerate(employee_list):
        employee_list[i].check_company_name()
        employee_list[i].check_clearances()
        employee_list[i].check_dept_num()
    
    return employee_list