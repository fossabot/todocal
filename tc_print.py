# TodoCal Print Functions

import tc_time
import tc_data
import tc_handler

def print_week_defaults ():
    TIME_INFO = tc_time.get_time_info ()
    DATA = tc_data.DATA
    summary = tc_handler.summarize_defaults (DATA, TIME_INFO)

    for e in summary:
        print (u'\u001b[38;5;' + e ["color"] + 'm' +
                "{month}/{day} {time} {name}".format (
                    month = e ["month"],
                    day = e ["day"],
                    time = e ["hour"].replace (' ', ':'),
                    name = e ["name"] )
                + u'\u001b[0m')

    return 0

def print_week_todos ():
    TIME_INFO = tc_time.get_time_info ()
    DATA = tc_data.DATA
    summary = tc_handler.summarize_todos (DATA, TIME_INFO)

    for e in summary:
        print (u'\u001b[38;5;' + e ["color"] + 'm' +
                "{month}/{day} {time} {name}".format (
                    month = e ["month"],
                    day = e ["day"],
                    time = e ["hour"].replace (' ', ':'),
                    name = e ["name"] )
                + u'\u001b[0m')

    return 0
