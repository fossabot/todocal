# TodoCal Handle Calendar Display
# -------------------------------
# (display module has higher hierarchy than print module)

from tc_print import pass_info # returns event list, dimension raw info, TIME_INFO
import tc_meta
import datetime
from textwrap import *

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
    # spans is int list

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
            weekday_below_row += (("{filler:^" + str(col_width) + "}").format (filler = ('-' * (col_width - 4))))
        return (weekday_row, weekday_below_row)
    (weekday_row, weekday_below_row) = make_weekday_row ()

    DISPLAY.append (weekday_row)
    DISPLAY.append (weekday_below_row + "\u001b[0m")
    # Above: first three rows of calendar display

    # first event re-synthesis
    E_SYNs = [[], [], [], [], [], [], []] # events re-synthesized by weekdays
    for e in synthesis:
        E_SYNs [e ["weekday"]].append (e)
    for L in E_SYNs: # sort events in each bucket by time-start-code (int)
        sorted (L, key = lambda e : (e ["time-start-code"] * 10000 + e ["time-end-code"]))

    # second event re-synthesis
    SYNs_DICT = [] # re-synthesized: in each weekday sort events in buckets by time-start-code
    for _ in range(7):
        E_DICT = {}
        for hour in spans:
            E_DICT [hour] = [] # initialize each bucket (hour span in weekday)
        SYNs_DICT.append (E_DICT)
    # put events in re-synthesis
    for i in range(7):
        L = E_SYNs [i] # address event list by reference in first re-synthesis
        D = SYNs_DICT [i] # address event dict by reference in second re-synthesis
        # transfer events in first re-syn to second re-syn
        for e in L:
            hour_code = e ["time-start-code"] // 100
            D [hour_code].append (e) # span bucket include this event
    # SYNs_DICT is list of dictionaries of (hour span int, event list) as (key, value)

    T = TextWrapper ()
    T.width = col_width
    T.initial_indent = "* "

    # making event display with col_width, span_height (for one weekday bucket)
    def make_main_display (col_width, span_height, DICT, T):
        # ensure span_height allow all events normal display
        for (span_hour, E) in DICT.items ():
            if len(E) > span_height:
                tc_meta.raise_ERROR ("TodoCal: calendar height too small.")
            else:
                continue
        COL = [] # make list of strings for this column display
        for span_hour in sorted (DICT): # access span hour event lists in order
            E = DICT [span_hour] # access to event list
            if len(E) == 0:
                for _ in span_height: # fill span hour height with white space
                    COL.append (' ' * col_width)
                continue
            # handle actual events
            individual_span = span_height // (len(E))
            assert (individual_span >= 1)
            count_use_span = 0
            for e in E:
                e_display = T.wrap (e ["name"]) # return string list of <= col_width
                if len(e_display) > individual_span: # event overflows height
                    e_display = e_display [:individual_span] # slice excess
                    last_line = e_display [-1]
                    if ' ' not in last_line:
                        last_line = "..."
                    else:
                        white_space_index = last_line.rfind (' ')
                        last_line = last_line [:white_space_index] + "..."
                    e_display [-1] = last_line # update last line in display
                    assert (len(e_display) == individual_span)
                for line in e_display:
                    COL.append ('\u001b[38;5;' + e ["color-code"] + 'm' +
                                ('{line_str:<' + col_width + '}').format (line_str = line) +
                                '\u001b[0m')
                    count_use_span += 1
            for _ in range(span_height - count_use_span): # fill un-used height
                COL.append (' ' * col_width)
            continue
        assert (len(COL) == span_height * len(spans))
        return COL # encoded with color information

    COLs = [[], [], [], [], [], [], []]
    for i in range(7):
        COLs [i] = make_main_display (col_width, span_height, SYNs_DICT [i], T)

    ROWs = [(' ' + COLs[0][i] +
            ' ' + COLs[1][i] +
            ' ' + COLs[2][i] +
            ' ' + COLs[3][i] +
            ' ' + COLs[4][i] +
            ' ' + COLs[5][i] +
            ' ' + COLs[6][i]) for i in range (len (COLs[0]))]
    for i in range(len(ROWs)):
        if i % span_height == 0:
            hour_index = i // span_height
            ROWs [i] = (' {hour:>2}:00 '.format (hour = spans [hour_index])) + ROWs [i]
        else:
            ROWs [i] = "   :   " + ROWs [i]

    for r in ROWs:
        DISPLAY.append (r)

    return DISPLAY

