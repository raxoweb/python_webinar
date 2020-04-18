month_name = ["jan", "feb", "mar", "apr", "jun", "jul",
              "aug", "sept", "oct", "nov", "dec"]

hash_months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
    }

weekdays = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
    }

days_num = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
    "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10,
    "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14,
    "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18,
    "nineteenth": 19, "twentieth": 20, "twenty-first": 21, "twenty-second": 22,
    "twenty-third": 23, "twenty-fourth": 24, "twenty-fifth": 25,
    "twenty-sixth": 26, "twenty-seventh": 27, "twenty-eighth": 28,
    "twenty-ninth": 29, "thirtieth": 30, "thirty-first": 31,

    "one": 1,
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "twenty one": 21, "twenty two": 22, "twenty three": 23,
    "twenty four": 24, "twenty five": 25, "twenty six": 26, "twenty seven": 27,
    "twenty eight": 28, "twenty nine": 29, "thirty": 30, "thirty one": 31,
    'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
    'hundred': 100, 'thousand': 1000
}

date_sets = {"relative_dates": ["day", "date",
                                "day before yesterday", "ytd", "mtd"],
             "day": ["mon", "tues", "wed", "thu", "fri", "sat", "sun", "fortnight"],
             "quarter": ["quarter", "qtr1", "qtr2", "qtr3", "qtr4", "q1", "q2", "q3", "q4",
                         "qt1", "qt2", "qt3", "qt4"]}

# Supporting words for regex

num_supp = "(st|nd|rd|th)"
quarter = "(qtr1|qtr2|qtr3|qtr4|q1|q2|q3|q4|qt1|qt2|qt3|qt4)"
numbers = r"(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
          eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
          eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
          ninety|hundred|thousand)"
num = "(first|second|third|fourth|fifth|sixth|seventh| \
          eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth| \
          seventeenth|eighteenth|nineteenth|twentieth|twenty-first|twenty-second|twenty-third| \
          twenty-fourth|twenty-fifth|twenty-sixth|twenty-seventh|twenty-eighth|twenty-ninth| \
          thirtieth|thirty-first)"          

week_day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"

month_value = "(january|february|march|april|may|june|july|august|september| \
          october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)"

dmy = "(year|day|week|month|leap year|quarter)"
day_mon_years = {
    "years": "year",
    "months": "month",
    "weeks": "week",
    "days": "day"
}

rel_day = "(today|yesterday|tomorrow|tonight|tonite)"

exp1 = "(before|after|earlier|later|ago)"

q_num = "(first|second|third|fourth)"

exp2 = "(since|this|next|last|first|last to last|previous|before|after|past)"

support_word = ("from", "to", "between", "of", "for",)
