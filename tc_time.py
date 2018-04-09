# TodoCal Time Handler

import datetime

def get_time_info ():
    now = datetime.datetime.now ()

    month   = now.month      # numerical month
    day     = now.day        # numerical day
    hour    = now.hour       # numerical current hour
    minute  = now.minute     # numerical current minute
    weekday = now.weekday () # numerical weekday

    if minute < 10: # ignore minute
        hour = str (hour)
    elif minute > 50: # round up hour
        hour = str (hour + 1)
    else:
        hour = str (hour) + " " + str (minute)

    if weekday == 6: # adjust weekday
        weekday = 0
    else:
        weekday += 1

    # week_start is always Sunday, week_end is always Saturday
    week_start = now -        datetime .timedelta (days = weekday) # use adjusted weekday
    week_end   = week_start + datetime .timedelta (days = 6)

    TIME_INFO = {
            "month"            : month,            # int
            "day"              : day,              # int
            "hour"             : hour,             # string
            "weekday"          : weekday,          # int
            "week-start-month" : week_start.month, # int
            "week-start-day"   : week_start.day,   # int
            "week-end-month"   : week_end.month,   # int
            "week-end-day"     : week_end.day,     # int
            }
    return TIME_INFO

