# TodoCal Event Handler

# filtering : exclude events outside of current week span
# convertion : convert all into no-repeat default or todo events

import datetime

def day_in_week (TIME_INFO, month, day):
    week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
    week_end_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-end-month"], TIME_INFO ["week-end-day"])
    event_date_object = datetime.date (TIME_INFO ["year"], month, day)
    return week_start_date_object <= event_date_object <= week_end_date_object

def convert_hours (whole_day, hour, length):
    if whole_day == "no":
        return (hour, length)
    else:
        return ("0", str (24 * 60))

def import_yearly_default (DATA, TIME_INFO):
    yearly_defaults = DATA ["events"] ["yearly"] ["default"] # un-filtered, un-converted
    filtered = [event for event in yearly_defaults if day_in_week (TIME_INFO, int (event["month"]), int (event["day"]))]

    converted = [{"name" : e["name"], "month" : e["month"], "day" : e["day"],
        "hour" : convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
        "length" : convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]

    return converted

def import_yearly_todo (DATA, TIME_INFO):
    yearly_todo = DATA ["events"] ["yearly"] ["todo"] # un-filtered, un-converted
    filtered = [event for event in yearly_todo if day_in_week (TIME_INFO, int (event["month"]), int (event["day"]))]

    converted = [{"name" : e["name"], "month" : e["month"], "day" : e["day"], "done" : e["done"],
        "hour" : convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
        "length" : convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]

    return converted
