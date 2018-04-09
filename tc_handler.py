# TodoCal Event Handler

# filtering : exclude events outside of current week span
# convertion : convert all into no-repeat default or todo events

import datetime

def day_in_week (TIME_INFO, month, day):
    week_start_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-start-month"], TIME_INFO ["week-start-day"])
    week_end_date_object = datetime.date (TIME_INFO ["year"], TIME_INFO ["week-end-month"], TIME_INFO ["week-end-day"])
    event_date_object = datetime.date (TIME_INFO ["year"], month, day)
    return week_start_date_object <= event_date_object <= week_end_date_object

def import_yearly_default (DATA, TIME_INFO):
    yearly_defaults = DATA ["events"] ["yearly"] ["default"] # un-filtered, un-converted
    filtered = [event for event in yearly_defaults if day_in_week (TIME_INFO, int (event["month"]), int (event["day"]))]

    converted = []
    for event in filtered:
        convertion = {}
        convertion ["name"]  = event ["name"]
        convertion ["month"] = event ["month"]
        convertion ["day"]   = event ["day"]
        if event ["whole-day"] == "yes":
            convertion ["hour"]   = "0"
            convertion ["length"] = str (24 * 60)
        else:
            convertion ["hour"]   = event ["hour"]
            convertion ["length"] = event ["length"]
        converted.append (convertion)

    return converted

