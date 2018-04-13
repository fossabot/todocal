# TodoCal Event Handler

# filtering : exclude events outside of current week span
# convertion : convert all into no-repeat default or todo events

# Catelog
# summarize_defaults (DATA, TIME_INFO): return summary (event list object)
# summarize_todos --

import datetime

def __day_in_week (TIME_INFO, month, day):
    week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
    week_end_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-end-month"], TIME_INFO ["week-end-day"])
    event_date_object = datetime.date (TIME_INFO ["year"], month, day)
    return week_start_date_object <= event_date_object <= week_end_date_object

def __convert_hours (whole_day, hour, length):
    if whole_day == "no":
        return (hour, length)
    else:
        return ("0", str (24 * 60))

def __import_yearly_default (DATA, TIME_INFO):
    yearly_defaults = DATA ["events"] ["yearly"] ["default"] # un-filtered, un-converted
    filtered = [event for event in yearly_defaults if __day_in_week (TIME_INFO, int (event["month"]), int (event["day"]))]

    converted = [{"name" : e["name"], "month" : e["month"], "day" : e["day"],
        "hour" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
        "length" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]

    return converted

def __import_yearly_todo (DATA, TIME_INFO):
    yearly_todo = DATA ["events"] ["yearly"] ["todo"] # un-filtered, un-converted
    filtered = [event for event in yearly_todo if __day_in_week (TIME_INFO, int (event["month"]), int (event["day"]))]

    converted = [{"name" : e["name"], "month" : e["month"], "day" : e["day"], "done" : e["done"],
        "hour" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
        "length" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]

    return converted

def __import_monthly_default (DATA, TIME_INFO):
    monthly_default = DATA ["events"] ["monthly"] ["default"] # un-filtered, un-converted

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        filtered = [event for event in monthly_default if __day_in_week (TIME_INFO, TIME_INFO ["month"], int (event["day"]))]
    else:
        filtered = []
        for event in monthly_default:
            if __day_in_week (TIME_INFO, TIME_INFO ["week-start-month"], int (event["day"])):
                filtered.append ((event, "week-start-month")) # use a tuple to indicate which month
            elif __day_in_week (TIME_INFO, TIME_INFO ["week-end-month"], int (event["day"])):
                filtered.append ((event, "week-end-month"))
            else:
                continue

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        converted = [{"name" : e["name"], "month" : str (TIME_INFO["month"]), "day" : e["day"],
            "hour" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
            "length" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]
    else:
        converted = [{"name" : t[0]["name"], "month" : str (TIME_INFO[t[1]]), "day" : t[0]["day"],
            "hour" : __convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [0],
            "length" : __convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [1]} for t in filtered]

    return converted

def __import_monthly_todo (DATA, TIME_INFO):
    monthly_todo = DATA ["events"] ["monthly"] ["todo"] # un-filtered, un-converted

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        filtered = [event for event in monthly_todo if __day_in_week (TIME_INFO, TIME_INFO ["month"], int (event["day"]))]
    else:
        filtered = []
        for event in monthly_todo:
            if __day_in_week (TIME_INFO, TIME_INFO ["week-start-month"], int (event["day"])):
                filtered.append ((event, "week-start-month")) # use a tuple to indicate which month
            elif __day_in_week (TIME_INFO, TIME_INFO ["week-end-month"], int (event["day"])):
                filtered.append ((event, "week-end-month"))
            else:
                continue

    if TIME_INFO ["week-start-month"] == TIME_INFO ["week-end-month"]:
        converted = [{"name" : e["name"], "month" : str (TIME_INFO["month"]), "day" : e["day"], "done" : e["done"],
            "hour" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [0],
            "length" : __convert_hours (e["whole-day"], e["hour"], e["length"]) [1]} for e in filtered]
    else:
        converted = [{"name" : t[0]["name"], "month" : str (TIME_INFO[t[1]]), "day" : t[0]["day"], "done" : t[0]["done"],
            "hour" : __convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [0],
            "length" : __convert_hours (t[0]["whole-day"], t[0]["hour"], t[0]["length"]) [1]} for t in filtered]

    return converted

def __import_weekly_default (DATA, TIME_INFO):
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

def __import_weekly_todo (DATA, TIME_INFO):
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

def __import_daily_default (DATA, TIME_INFO):
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

def __import_daily_todo (DATA, TIME_INFO):
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

def __get_color_code (DATA, request):
    try:
        [category, status] = [msg for msg in request.split (' ')]
    except:
        print ('\u001b[31mUnexpected Error.\u001b[0m')
    assignment = DATA ['meta'] ['color']
    try:
        category_colors = assignment [category]
    except:
        print ('\u001b[31mUnexpected Error.\u001b[0m')
    colors = [name for name in category_colors.split (' ')]
    try:
        default_color = colors[0]
        todo_color = colors [1]
        late_color = colors [2]
    except:
        print ('\u001b[31mUnexpected Error.\u001b[0m')
    try:
        default_color_code = DATA ['meta'] ['color-code'] [default_color]
        todo_color_code = DATA ['meta'] ['color-code'] [todo_color]
        late_color_code = DATA ['meta'] ['color-code'] [late_color]
    except:
        print ('\u001b[31mUnexpected Error.\u001b[0m')
    if status == 'default':
        return default_color_code
    if status == 'todo':
        return todo_color_code
    if status == 'late':
        return late_color_code
    return '015' # white

def summarize_defaults (DATA, TIME_INFO):
    yearly_defaults  = __import_yearly_default (DATA, TIME_INFO)
    monthly_defaults = __import_monthly_default (DATA, TIME_INFO)
    weekly_defaults  = __import_weekly_default (DATA, TIME_INFO)
    daily_defaults   = __import_daily_default (DATA, TIME_INFO)
    no_rep_defaults  = [event for event in DATA ["events"] ["no-repeat"] ["default"]]

    yearly_color  = __get_color_code (DATA, "yearly default")
    monthly_color = __get_color_code (DATA, "monthly default")
    weekly_color  = __get_color_code (DATA, "weekly default")
    daily_color   = __get_color_code (DATA, "daily default")
    no_rep_color  = __get_color_code (DATA, "no-repeat default")

    for e in yearly_defaults:
        e ["color"] = yearly_color
    for e in monthly_defaults:
        e ["color"] = monthly_color
    for e in weekly_defaults:
        e ["color"] = weekly_color
    for e in daily_defaults:
        e ["color"] = daily_color
    for e in no_rep_defaults:
        e ["color"] = no_rep_color

    summary = yearly_defaults + monthly_defaults + weekly_defaults + daily_defaults + no_rep_defaults

    for event in summary: # type checking
        assert (type (event["name"])   == str)
        assert (type (event["month"])  == str)
        assert (type (event["day"])    == str)
        assert (type (event["hour"])   == str)
        assert (type (event["length"]) == str)

    return summary

def summarize_todos (DATA, TIME_INFO):
    yearly_todos  = __import_yearly_todo (DATA, TIME_INFO)
    monthly_todos = __import_monthly_todo (DATA, TIME_INFO)
    weekly_todos  = __import_weekly_todo (DATA, TIME_INFO)
    daily_todos   = __import_daily_todo (DATA, TIME_INFO)
    no_rep_todos  = [event for event in DATA ["events"] ["no-repeat"] ["todo"]]

    yearly_todo_color  = __get_color_code (DATA, "yearly todo")
    yearly_late_color  = __get_color_code (DATA, "yearly late")
    monthly_todo_color = __get_color_code (DATA, "monthly todo")
    monthly_late_color = __get_color_code (DATA, "monthly late")
    weekly_todo_color  = __get_color_code (DATA, "weekly todo")
    weekly_late_color  = __get_color_code (DATA, "weekly late")
    daily_todo_color   = __get_color_code (DATA, "daily todo")
    daily_late_color   = __get_color_code (DATA, "daily late")
    no_rep_todo_color  = __get_color_code (DATA, "no-repeat todo")
    no_rep_late_color  = __get_color_code (DATA, "no-repeat late")

    current_datetime_object = datetime.datetime (
        TIME_INFO ["year"], TIME_INFO ["month"], TIME_INFO ["day"],
        [int (s) for s in TIME_INFO ["hour"].split(' ')][0] )

    def is_late (event):
        event_datetime_object = datetime.datetime (
            TIME_INFO ["year"], int (event ["month"]), int (event ["day"]),
            [int (s) for s in event ["hour"].split(' ')][0] )
        return current_datetime_object > event_datetime_object

    for e in yearly_todos:
        if is_late (e):
            e ["color"] = yearly_late_color
        else:
            e ["color"] = yearly_todo_color
    for e in monthly_todos:
        if is_late (e):
            e ["color"] = monthly_late_color
        else:
            e ["color"] = monthly_todo_color
    for e in weekly_todos:
        if is_late (e):
            e ["color"] = weekly_late_color
        else:
            e ["color"] = weekly_todo_color
    for e in daily_todos:
        if is_late (e):
            e ["color"] = daily_late_color
        else:
            e ["color"] = daily_todo_color
    for e in no_rep_todos:
        if is_late (e):
            e ["color"] = no_rep_late_color
        else:
            e ["color"] = no_rep_todo_color

    summary = yearly_todos + monthly_todos + weekly_todos + daily_todos + no_rep_todos

    for event in summary: # type checking
        assert (type (event["name"])   == str)
        assert (type (event["month"])  == str)
        assert (type (event["day"])    == str)
        assert (type (event["hour"])   == str)
        assert (type (event["length"]) == str)
        assert (type (event["done"])   == str)

    return summary

