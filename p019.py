## Find the number of firsts of the month that were Sundays in the 20th century

import datetime

SUNDAY = 6

def p019():
    return sum((datetime.datetime(year, month, 1).weekday() == SUNDAY)
            for year in range(1901,2001)
            for month in range(1,13))
