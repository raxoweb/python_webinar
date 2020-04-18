from WordNet import *

# Regex ....
iso = r"\d+[/-]\d+[/-]\d+ \d+:\d+:\d+\.\d+"
    
date = r"[\d]{1,2}/[\d]{1,2}/[\d]{4}|[\d]{1,2}-[\d]{1,2}-[\d]{2,4}|[\d]{1," \
       "2}\s(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s[\d]{4}|[\d]{1," \
       "2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s[\d]{4}"

year = r"((?<=\s)\d{4}|^\d{4})"

reg_expression1 = r"((\d+" + num_supp + "?" + "|(" + numbers + r"[-\s]?)) " + dmy + "s? " + exp1 + ")"

reg_expression2 = "(" + exp2 + "( " + dmy + "))"
reg_expression7 = "(" + exp2 + "( " + week_day + "))"
reg_expression8 = "(" + exp2 + "( " + month_value + "))"
reg_expression3 = "(" + exp2 + r" \d{4})"

reg_expression4 = "(" + exp2 + " (" + r"\d+" + "|" + numbers + ")" + " (" + dmy + "|" + week_day + "|" + month_value + ")) "

reg_expression5 = "(" + exp2 + r" \d{1,2}$)"

reg_expression6 = "([1-4]" + num_supp + r"([-\s]?)" + dmy + "s?" + ")"

regex_quarter1 = "(" + q_num + r"([-\s]?)+quarter)"

regex_quarter2 = r"(quarter([-\s]?)[1-4])"

regex_quarter3 = "(" + quarter + ")"

regex_quarter4 = "([1-4]" + num_supp + r"([-\s]?)quarter)"

regex_from_to = r"(from\s(" + date + r")\sto\s(" + date + "))"

date_validate1 = '(3[01]|[12][0-9]|0[1-9])/(' + month_value + ')/([0-9]{4})$'

date_validate2 = '(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0?[1-9])/([0-9]{4})$'


relative_date = r"((19|20)\d{2}(\s)+"+month_value+")"

relative_date1 = r"(\sago|\sin|\sfrom\snow|tomorrow|today|yesterday|year|\d\syear(s)?|\d\smonth(s)?|\d\sweek(s)?|\d\sday(s)?)"

relative_date2 = r"(last|last\s\d)\s" + week_day

relative_date3 = r"((after|since)\s((19|20)\d{2}|(sunday|monday|tuesday)))"

month_year_val = r"("+month_value+r"\s+(19|20)\d{2})"


between_date = r'(between\s.+(\d{4}|\d{2}).*and.+(\d{4}|\d{2}).+)'

and_date = r'((\d{4}.*)|([/\-.]\d{2}))(?=\sand.+((\d{4}.*)|([/\-.]\d{2})))'

from_to = r'from\s.+(\d{4}|\d{2}).*to.+(\d{4}|\d{2})'

year_date = r'(?<=\s)19[0-9]{2}(?=\s)|(?<=\s)20[0-9]{2}(?![-,/\\:a-zA-Z])'

year_with_month =r'19[0-9]{2}|20[0-9]{2}(?![-,/\\:a-zA-Z])(?=\s+'+month_value+')'

month_with_year =''+month_value+r'(?=(\s+19[0-9]{2}|\s+20[0-9]{2})(?![-,/\\:a-zA-Z]))'

year_num_date = r'(?<!\d{2}\s)\d{4}(?!\s\d{2})'

since_date = r'((?<=since\s)\d{4})|((?<=since\s)' + month_value + ')'

since_year = r"(?<=since\s)\d{4}"

since_dmy = r"(since|past)\s\d+\s(year|quarter|month)(s)?"

dmy_ago = r"\d+\s(month|year|quarter)(s)?\sago"

today_yesterday_val = r'today|yesterday'

parse_year = r'(\d{4}[-/]\d{2}[-/]\d{2})'

week_num_val = r'([0-9]{1,2})\s' + week_day+''

parse_month = r"since\s{MONTH_IN_WORDS}"
