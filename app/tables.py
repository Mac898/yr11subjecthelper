# import things
from flask_table import Table, Col

# Declare your table
class WeekATable(Table):
    WA_PID = Col('Period')
    WA_MON = Col('Monday')
    WA_TUE = Col('Tuesday')
    WA_WED = Col('Wednesday')
    WA_THU = Col('Thursday')
    WA_FRI = Col('Friday')

class WeekBTable(Table):
    WA_PID = Col('Period')
    WB_MON = Col('Monday')
    WB_TUE = Col('Tuesday')
    WB_WED = Col('Wednesday')
    WB_THU = Col('Thursday')
    WB_FRI = Col('Friday')