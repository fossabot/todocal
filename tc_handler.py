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

def import_monthly_default (DATA, TIME_INFO):
    monthly_default = DATA ["events"] ["monthly"] ["default"] # un-filtered, un-converted

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        filtered = [event for event in monthly_default if day_in_week (TIME_INFO, TIME_INFO ["month"], int (event["day"]))]
    else:
        filtered = []
        for event in monthly_default:
            if day_in_week (TIME_INFO, TIME_INFO ["week-start-month"], int (event["day"])):
                filtered.append ((event, "week-start-month")) # use a tuple to indicate which month
            elif day_in_week (TIME_INFO, TIME_INFO ["week-end-month"], int (event["day"])):
                filtered.append ((event, "week-end-month"))
            else:
                continue

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        converted = [{"name" : e["name"], "month" : str (TIME_INFO["month"]), "day" : e["day"],
            "hour" : convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
            "length" : convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]
    else:
        converted = [{"name" : t[0]["name"], "month" : str (TIME_INFO[t[1]]), "day" : t[0]["day"],
            "hour" : convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [0],
            "length" : convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [1]} for t in filtered]

    return converted

def import_monthly_todo (DATA, TIME_INFO):
    monthly_todo = DATA ["events"] ["monthly"] ["todo"] # un-filtered, un-converted

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        filtered = [event for event in monthly_todo if day_in_week (TIME_INFO, TIME_INFO ["month"], int (event["day"]))]
    else:
        filtered = []
        for event in monthly_todo:
            if day_in_week (TIME_INFO, TIME_INFO ["week-start-month"], int (event["day"])):
                filtered.append ((event, "week-start-month")) # use a tuple to indicate which month
            elif day_in_week (TIME_INFO, TIME_INFO ["week-end-month"], int (event["day"])):
                filtered.append ((event, "week-end-month"))
            else:
                continue

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        converted = [{"name" : e["name"], "month" : str (TIME_INFO["month"]), "day" : e["day"], "done" : e["done"],
            "hour" : convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
            "length" : convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]
    else:
        converted = [{"name" : t[0]["name"], "month" : str (TIME_INFO[t[1]]), "day" : t[0]["day"], "done" : t[0]["done"],
            "hour" : convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [0],
            "length" : convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [1]} for t in filtered]

    return converted

def import_weekly_default (DATA, TIME_INFO):
    # no need for filtering
    # convertion based on weekday
    weekly_defaults = DATA ["events"] ["weekly"] ["default"]
    def get_date (event):
        weekday = event ["day"]
        week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
        event_date_object = week_start_date_object + datetime.timedelta (days = int (weekday))
        month = str (event_date_object.month)
        day = str (event_date_object.day)
        return (month, day)
    converted = [{"name" : e["name"], "month" : get_date(e)[0], "day" : get_date(e)[1],
        "hour" : e["hour"], "length" : e["length"]} for e in weekly_defaults]
    return converted

def import_weekly_todo (DATA, TIME_INFO):
    # no need for filtering
    # convertion based on weekday
    weekly_todo = DATA ["events"] ["weekly"] ["todo"]
    def get_date (event):
        weekday = event ["day"]
        week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
        event_date_object = week_start_date_object + datetime.timedelta (days = int (weekday))
        month = str (event_date_object.month)
        day = str (event_date_object.day)
        return (month, day)
    converted = [{"name" : e["name"], "month" : get_date(e)[0], "day" : get_date(e)[1], "done" : e["done"],
        "hour" : e["hour"], "length" : e["length"]} for e in weekly_todo]
    return converted

def import_daily_default (DATA, TIME_INFO):
    # duplicate event across all weekdays
    daily_default = DATA ["events"] ["daily"] ["default"]
    expanded = []
    week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
    for weekday in range(7): # from 0 to 6
        date_object = week_start_date_object + datetime.timedelta (days = weekday)
        month = str (date_object.month)
        day = str (date_object.day)
        for event in daily_default:
            expanded.append ({"name" : event["name"], "month" : month, "day" : day,
                "hour" : event["hour"], "length" : event["length"]})
    return expanded

def import_daily_todo (DATA, TIME_INFO):
    # duplicate event across all weekdays
    daily_todo = DATA ["events"] ["daily"] ["todo"]
    expanded = []
    week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
    for weekday in range(7): # from 0 to 6
        date_object = week_start_date_object + datetime.timedelta (days = weekday)
        month = str (date_object.month)
        day = str (date_object.day)
        for event in daily_todo:
            done_dates = [int (d) for d in event["done"].split(" ")]
            if weekday in done_dates:
                done = "yes"
            else:
                done = "no"
            expanded.append ({"name" : event["name"], "month" : month, "day" : day, "done" : done,
                "hour" : event["hour"], "length" : event["length"]})
    return expanded

def summarize_defaults (DATA, TIME_INFO):
    yearly_defaults  = import_yearly_default (DATA, TIME_INFO)
    monthly_defaults = import_monthly_default (DATA, TIME_INFO)
    weekly_defaults  = import_weekly_default (DATA, TIME_INFO)
    daily_defaults   = import_daily_default (DATA, TIME_INFO)
    no_rep_defaults  = [event for event in DATA ["events"] ["no-repeat"] ["default"]]
    summary = yearly_defaults + monthly_defaults + weekly_defaults + daily_defaults + no_rep_defaults

    for event in summary: # type checking
        assert (type (event["name"])   == str)
        assert (type (event["month"])  == str)
        assert (type (event["day"])    == str)
        assert (type (event["hour"])   == str)
        assert (type (event["length"]) == str)

    return summary

def summarize_todos (DATA, TIME_INFO):
    yearly_todos  = import_yearly_todo (DATA, TIME_INFO)
    monthly_todos = import_monthly_todo (DATA, TIME_INFO)
    weekly_todos  = import_weekly_todo (DATA, TIME_INFO)
    daily_todos   = import_daily_todo (DATA, TIME_INFO)
    no_rep_todos  = [event for event in DATA ["events"] ["no-repeat"] ["todo"]]
    summary = yearly_todos + monthly_todos + weekly_todos + daily_todos + no_rep_todos

    for event in summary: # type checking
        assert (type (event["name"])   == str)
        assert (type (event["month"])  == str)
        assert (type (event["day"])    == str)
        assert (type (event["hour"])   == str)
        assert (type (event["length"]) == str)
        assert (type (event["done"])   == str)

    return summary

