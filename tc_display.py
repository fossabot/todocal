# TodoCal Handle Calendar Display
# -------------------------------
# Display handler creates string list for print module to display.

from tc_print import pass_info # returns event list, dimension raw info, TIME_INFO
import tc_meta
import datetime

def __get_dimension_info (raw_info): # dimension raw info passed from pass_info
    try:
        cell_width = int (raw_info ["cell-width"])
    except:
        try:
            cell_width = int (raw_info ["max-width"]) // 8
        except:
            tc_meta.raise_ERROR ("Error: calendar dimensions not well defined.")

    if cell_width <= 7:
        tc_meta.raise_ERROR ("TodoCal: unimplemented situation.")
    # assert (cell_width >= 8)

    time_col_width = 7 # allow full time display
    between_col_width = 1
    col_width = cell_width

    calendar_width = time_col_width + col_width * 7 + between_col_width * 7

    try:
        max_height = int (raw_info ["max-height"])
    except:
        tc_meta.raise_ERROR ("Error: calendar dimensions not well defined.")

    return (calendar_width, max_height, (time_col_width, between_col_width, col_width))

def __get_calendar_height (max_height, E): # max_height passed from __get_dimension_info
    # information in e in E (passed from pass_info)
    # name, month, day, hour, length, (done), mark (0/1 char), color (str)

    for e in E:

        # code segment first copy ---------------------------------------------
        if ' ' not in e ["hour"]:
            e ["hour"] += " 00"
        e ["time-start-code"] = int (e ["hour"].replace (' ', ''))
        try:
            start_time = [int (s) for s in e ["hour"].split (' ')]
            start_hour = start_time [0]
            start_minute = start_time [1]
        except:
            tc_meta.raise_ERROR ("TodoCal: time convertion error.")
        start_time_object = datetime.time (hour = start_hour, minute = start_minute)
        start_time_object = datetime.datetime (year = 2000, month = 1, day = 1,
                                                            hour = start_time_object.hour,
                                                            minute = start_time_object.minute) # convert time to datetime
        try:
            if e ["length"] == "":
                end_time_object = start_time_object
            else:
                end_time_object = start_time_object + datetime.timedelta (minutes = int (e ["length"]))
        except:
            tc_meta.raise_ERROR ("TodoCal: time calculation error.")
        time_end_code = end_time_object.hour * 100 + end_time_object.minute
        if time_end_code < e ["time-start-code"]:
            time_end_code = 2359
        if time_end_code != 0 and time_end_code % 100 == 0:
            time_end_code -= 41 # reduce to past hour
        e ["time-end-code"] = time_end_code
        # code segment end ----------------------------------------------------
    # e.g. hour = "15 20", length = "30"
    # time-start-code = 1520, time-end-code = 1550

    span_mark = []
    for _ in range(24):
        span_mark.append (0)
        # span_mark [i] => time from i hour to (i + 1) hour
    for e in E:
        for i in range (e ["time-start-code"] // 100, e ["time-end-code"] // 100 + 1):
            span_mark [i] = 1
    spans = []
    for i in range(24):
        if span_mark [i] == 1:
            spans.append (i)
    # e.g. spans = [0, 7, 8, 10, 15]
    # => exist events in 0-1, 7-9, 10-11, 15-16

    available_height = max_height - 3 # reserve top rows for calendar header
    span_height = available_height // (len (spans))

    if span_height <= 1:
        tc_meta.raise_ERROR ("TodoCal: unimplemented situation.")
    # assert (span_height >= 2)

    calendar_height = span_height * (len (spans)) + 3
    return (calendar_height, span_height, spans)

def __prepare_events (E, TIME_INFO): # synthesize event information, return new list
    synthesis = []
    current_year = TIME_INFO ["year"]
    for e in E:
        new_info = {}
        new_info ["name"] = e ["name"] # new_info -> name
        if e ["mark"] != '':
            new_info ["name"] += (' ' + e ["mark"]) # include todo mark in event name
        event_date_object = datetime.datetime (year = current_year, month = int (e ["month"]), day = int (e ["day"]))
        weekday = event_date_object.isoweekday ()
        if weekday == 7:
            weekday = 0
        weekday = str (weekday)
        new_info ["weekday"] = int (weekday) # new_info -> weekday (int)
        new_info ["color-code"] = e ["color"] # new_info -> color-code (str)

        # code segment copy ---------------------------------------------------
        if ' ' not in e ["hour"]:
            e ["hour"] += " 00"
        e ["time-start-code"] = int (e ["hour"].replace (' ', ''))
        try:
            start_time = [int (s) for s in e ["hour"].split (' ')]
            start_hour = start_time [0]
            start_minute = start_time [1]
        except:
            tc_meta.raise_ERROR ("TodoCal: time convertion error.")
        start_time_object = datetime.time (hour = start_hour, minute = start_minute)
        start_time_object = datetime.datetime (year = 2000, month = 1, day = 1,
                                                            hour = start_time_object.hour,
                                                            minute = start_time_object.minute) # convert time to datetime
        try:
            if e ["length"] == "":
                end_time_object = start_time_object
            else:
                end_time_object = start_time_object + datetime.timedelta (minutes = int (e ["length"]))
        except:
            tc_meta.raise_ERROR ("TodoCal: time calculation error.")
        time_end_code = end_time_object.hour * 100 + end_time_object.minute
        if time_end_code < e ["time-start-code"]:
            time_end_code = 2359
        if time_end_code != 0 and time_end_code % 100 == 0:
            time_end_code -= 41 # reduce to past hour
        e ["time-end-code"] = time_end_code
        # code segment copy end -----------------------------------------------

        new_info ["time-start-code"] = e ["time-start-code"]
        new_info ["time-end-code"] = e ["time-end-code"]
        # new_info -> name, weekday (int), color-code (str), time-start-code (int), time-end-code (int)

        synthesis.append (new_info)
    return synthesis # synthesized new event list

def make_display ():
    (E, dimension_raw_info, TIME_INFO) = pass_info () # get data from print module

    synthesis = __prepare_events (E, TIME_INFO) # synthesized new event list
    # e in synthesis -> name, weekday (int), color-code (str), time-start/end-code (int)

    (calendar_width, max_height, (time_col_width, between_col_width, col_width)) = __get_dimension_info (dimension_raw_info)
    (calendar_height, span_height, spans) = __get_calendar_height (max_height, E)

# |---------------------- calendar width ---------------------------|
# |----time_col----|---------------(header)-------------------------|
# |................|------|------|------|------|------|------|------|
# => col_width = 6, between_col_width = 1 ..........................|
# | 8:00 | ---------> ..............................................|
# |......| .......... => span_height = 2 ...........................|
# | 9:00 | ---------> ..............................................|
# |_________________ calendar height (||) __________________________|
# Assumptions:
# time_col_width >= 7
# col_width      >= 8
# span_height    >= 2

    DISPLAY = [] # string list for calendar display (according to above)

    def make_calendar_heading ():
        heading = "TodoCal Week Summary"
        heading += ' '
        heading += "\u001b[36m"
        heading += (str(TIME_INFO ["week-start-month"]) + '/' + str(TIME_INFO ["week-start-day"]))
        heading += ' -- '
        heading += (str(TIME_INFO ["week-end-month"]) + '/' + str(TIME_INFO ["week-end-day"]))
        heading += "\u001b[0m"
        heading = (("{header:^" + str(calendar_width) + "}").format (header = heading))
        return heading
    DISPLAY.append (make_calendar_heading ())

    def make_weekday_row ():
        weekday_row = "\u001b[37m"
        weekday_below_row = ""
        weekday_row += (' ' * time_col_width)
        weekday_below_row += (' ' * time_col_width)
        weekdays = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
        for i in range(7):
            weekday_row += ' '
            weekday_below_row += ' '
            weekday_row += (("{weekday:^" + str(col_width) + "}").format (weekday = weekdays [i]))
            weekday_below_row += (("{filler:^" + str(col_width) + "}").format (filler = ('-' * (len(weekdays[i]) + 2))))
        return (weekday_row, weekday_below_row)
    (weekday_row, weekday_below_row) = make_weekday_row ()

    DISPLAY.append (weekday_row)
    DISPLAY.append (weekday_below_row + "\u001b[0m")

    return DISPLAY

