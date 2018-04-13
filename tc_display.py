# TodoCal Handle Calendar Display
# -------------------------------
# Display handler creates string list for print module to display.

from tc_print import pass_info
import tc_meta
import datetime

def __get_dimension_info (raw_info):
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

def __get_calendar_height (max_height, col_width, E):
    # information in e in E
    # name, month, day, hour, length, (done), mark (0/1 char)

    for e in E:
        if ' ' not in e ["hour"]:
            e ["hour"] += " 00"
    for e in E:
        e ["time-start-code"] = int (e ["hour"].replace (' ', ''))
        try:
            start_time = [int (s) for s in e ["hour"].split (' ')]
            start_hour = start_time [0]
            start_minute = start_time [1]
        except:
            tc_meta.raise_ERROR ("")
        start_time_object = datetime.time (hour = start_hour, minute = start_minute)
        try:
            if e ["length"] == "":
                end_time_object = start_time_object
            else:
                end_time_object = start_time_object + datetime.timedelta (minutes = int (e ["length"]))
        except:
            tc_meta.raise_ERROR ("")
        time_end_code = end_time_object.hour * 100 + end_time_object.minute
        if time_end_code < e ["time-start-code"]:
            time_end_code = 2359
        if time_end_code != 0 and time_end_code % 100 == 0:
            time_end_code -= 41 # reduce to past hour
        e ["time-end-code"] = time_end_code
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
