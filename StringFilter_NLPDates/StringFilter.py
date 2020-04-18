import re
from reg import *
import WordNet
import datefinder
from dateparser.search import search_dates
from timeit import Timer
import time

class TimeStringFilter:
    """docstring for found_value"""
    reg1 = re.compile(reg_expression1, re.IGNORECASE)
    reg2 = re.compile(reg_expression2, re.IGNORECASE)
    reg17 = re.compile(reg_expression7, re.IGNORECASE)
    reg18 = re.compile(reg_expression8, re.IGNORECASE)
    reg3 = re.compile(rel_day, re.IGNORECASE)
    reg4 = re.compile(iso)
    reg5 = re.compile(year)
    reg6 = re.compile(date)
    reg7 = re.compile(regex_quarter1, re.IGNORECASE)
    reg8 = re.compile(regex_quarter2, re.IGNORECASE)
    reg9 = re.compile(regex_quarter3, re.IGNORECASE)
    reg10 = re.compile(regex_quarter4, re.IGNORECASE)
    reg11 = re.compile(reg_expression4, re.IGNORECASE)
    reg12 = re.compile(reg_expression3, re.IGNORECASE)
    reg13 = re.compile(reg_expression5, re.IGNORECASE)
    reg14 = re.compile(reg_expression6, re.IGNORECASE)
    reg16 = re.compile(regex_from_to, re.IGNORECASE)

    RELATIVE_REG = re.compile(relative_date, re.IGNORECASE)  # to get false in date_is_relative
    RELATIVE_REG1 = re.compile(relative_date1, re.IGNORECASE)
    RELATIVE_REG2 = re.compile(relative_date2, re.IGNORECASE)
    RELATIVE_REG3 = re.compile(relative_date3, re.IGNORECASE)

    between_year = re.compile(between_date, re.IGNORECASE)
    and_date_value = re.compile(and_date, re.IGNORECASE)
    from_to_value = re.compile(from_to, re.IGNORECASE)
    year_value1 = re.compile(year_with_month, re.IGNORECASE) # year followed by month
    year_value2 = re.compile(month_with_year, re.IGNORECASE) # month followed by year
    year_value = re.compile(year_date, re.IGNORECASE) # find year value 
    date_num_value = re.compile(year_num_date, re.IGNORECASE)
    since_date_value = re.compile(since_date, re.IGNORECASE)
    since_year_value = re.compile(since_year, re.IGNORECASE)
    since_dmy_value = re.compile(since_dmy, re.IGNORECASE)
    dmy_ago_value = re.compile(dmy_ago, re.IGNORECASE)
    month_year_check = re.compile(month_year_val, re.IGNORECASE)  # need to be false in date_is_relative
    # Initialization
    time_found = []
    final_time = []
    time_text = ''

    def date_is_relative(self, translation):
        if not self.RELATIVE_REG.search(translation) and not self.month_year_check.search(
                translation) and self.RELATIVE_REG1.search(translation) and self.RELATIVE_REG2.search(
                translation) and self.RELATIVE_REG3.search(translation):
            return False
        else:
            return True

    def value_found(self, regex, text):
        found = regex.findall(text)
        # print(found)
        found = [a[0] for a in found if len(a) > 1]
        # print(found)
        # TODO // i have to manage continueous single value along with double value example: i want report for 
        # last year last month and also for last month then filter escape last month
        if len(found)== 1:
            self.time_found.append(found[0])
        else:    
            for i in range(0,len(found)):
                if self.time_found:
                    # print(found[i]," and value ",self.time_found[-1])
                    if re.search(found[i]+'$',self.time_found[-1]):
                        continue
                if i is not len(found)-1:
                    if re.search(r''+found[i]+r"\s+"+found[i+1],text):
                        self.time_found.append(found[i]+" "+found[i+1])
                    else:
                        self.time_found.append(found[i])             
                else:
                    if self.time_found:
                        if not re.search(found[i],self.time_found[-1]):
                            self.time_found.append(found[i])    
        
    def value_found2(self, regex, text):
        found = regex.findall(text)
        for time in found:
            self.time_found.append(time)

    def tag(self, text):
        relative_value = self.date_is_relative(text)
        if self.and_date_value.search(text) and not self.between_year.search(text) and not self.from_to_value.search(
                text) and relative_value:
            text = text.replace(', ', ',')
            if re.search(r'of\s+\d{4}', text):
                text = text.replace('of', 'another')
            text = text.replace('and', 'something')
            value = search_dates(text)
            if value and len(value) >= 1:
                self.time_found.append(value)
        year_reg1 = self.year_value1.findall(text)
        year_reg2 = self.year_value2.findall(text)
        year_reg  = self.year_value.findall(text) 
        month_reg = re.findall(r'' + month_value + '', text)
        number_reg = self.date_num_value.findall(text)
        since_value = self.since_date_value.findall(text)
        year_trigger = True
        if not (year_reg1 or year_reg2) and number_reg and not since_value and not self.from_to_value.search(text):
            year_trigger = False
            self.time_found.append(year_reg[0])
        if not (year_reg1 or year_reg2) and not since_value and month_reg:
            year_trigger = False
            self.time_found.append(month_reg[0])
        since_val = self.since_year_value.findall(text)
        since_num = self.since_dmy_value.findall(text)
        ago_val = self.dmy_ago_value.findall(text)
        if not since_val and not since_num and not ago_val and not since_value and not self.reg14.search(text):
            temp = list()
            if self.between_year.search(text):
                split_value = text.split('between')
                for value in split_value:
                    value = datefinder.find_dates(value, source=True)
                    for v in value:
                        temp.append(v)
                self.time_found.append(tuple(temp))
            elif year_trigger:
                date_val = datefinder.find_dates(text, source=True)
                if date_val:
                    
                    if self.from_to_value.search(text):
                        for value in date_val:
                            temp.append(value)
                           
                        self.time_found.append(tuple(temp))
                    else:
                        for value in date_val:
                    
                            self.time_found.append(value)
                            print("value for ",str(value[0]))        

        if self.reg2.search(text):
            self.value_found(self.reg2, text)

        if self.reg17.search(text):
            self.value_found(self.reg17, text)

        if self.reg18.search(text):
            self.value_found(self.reg18, text)

            # ex:- last 2
        if self.reg13.search(text):
            self.value_found(self.reg13, text)

        if self.reg1.search(text):
            self.value_found(self.reg1, text)
    
        # week
        if self.reg14.search(text):
            self.value_found(self.reg14, text)

        # today, tomorrow, etc
        if self.reg3.search(text):
            self.value_found2(self.reg3, text)

        # ISO
        if self.reg4.search(text):
            self.value_found2(self.reg4, text)


        # since|last num year|month
        if self.reg11.search(text):
            self.value_found(self.reg11, text)

        # since year
        if self.reg12.search(text):
            self.value_found(self.reg12, text)
    
        if self.reg16.search(text):
            self.value_found(self.reg16, text)
        # Date
        if self.reg6.search(text):
            self.value_found2(self.reg6, text)
        # quarter value
        if self.reg7.search(text):
            self.value_found(self.reg7, text)


        # quarter2 value
        if self.reg8.search(text):
            self.value_found(self.reg8, text)


        # quarter2 value
        if self.reg9.search(text):
            self.value_found(self.reg9, text)


        # quarter3 value
        if self.reg10.search(text):
            self.value_found(self.reg10, text)

        # Tag only temporal expressions which haven't been tagged.
        print("perfect value ",self.time_found)
       
        try:
            if any(ext in self.time_found for ext in WordNet.day_mon_years.keys()):
                sword = []
                time_value = ''
                for v in self.time_text.split():

                    if v in WordNet.day_mon_years.keys():
                        v = WordNet.day_mon_years[v]
                        sword.append(v)
                    else:
                        sword.append(v)
                for time in sword:
                    time_value = time_value + ' ' + time
                return time_value, time_value
            else:
                return self.time_text
        except Exception:
            return "", ""

today_yesterday = re.compile(today_yesterday_val, re.IGNORECASE)
ymd = re.compile(parse_year, re.IGNORECASE)
reg_week_num = re.compile(week_num_val, re.IGNORECASE)
reg_since_month = re.compile(parse_month, re.IGNORECASE)

if __name__ == '__main__':
    start = time.clock()
    string_val = "if you want last month first week and also for last month, this is last to last year and also for last leap year first month \
                  or more value of this year first month and this is last year last month you can also ask for \
                  last year ,this year is single value 2015 i think work for july also 25/11/2015."
    
    string_val = "i want report of july  and also for 2015 final check for 25/04/2015"

    time_string = TimeStringFilter()
    filter_value = time_string.tag(string_val)
    # print("Final value is ", filter_value)
    end = time.clock()
    print((end-start)*1000," milisecond")

