import datetime
from datetime import date, timedelta



#Helper function that will help to calculate the days in the period given
def days(start_date, end_date, serviceC = False):
    holidays = [5,6]
    day_count = 0

    start_date = start_date.split("-")
    end_date = end_date.split("-")

    start_date = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    end_date = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
    delta = timedelta(days=1)

    while start_date <= end_date:
        if not serviceC:
            if start_date.weekday() not in holidays:
                day_count += 1
        else:
            day_count += 1

        
        start_date += delta
    return day_count 







