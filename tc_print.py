# TodoCal Print Functions

import tc_time
import tc_data
import tc_handler

def __hour_to_time (hour):
    hour = hour.replace (' ', ':')
    if ':' not in hour:
        hour += ':00'
    return hour

def print_week_defaults ():
    TIME_INFO = tc_time.get_time_info ()
    DATA = tc_data.DATA
    summary = tc_handler.summarize_defaults (DATA, TIME_INFO)

    for e in summary:
        print (u'\u001b[38;5;' + e ["color"] + 'm' +
                "{month:>2}/{day:<2} {time:<5} {name:.>30}".format (
                    month = e ["month"],
                    day   = e ["day"],
                    time  = __hour_to_time (e ["hour"]),
                    name  = e ["name"] )
                + u'\u001b[0m')

    return 0

def print_week_todos ():
    TIME_INFO = tc_time.get_time_info ()
    DATA = tc_data.DATA
    summary = tc_handler.summarize_todos (DATA, TIME_INFO)

    for e in summary:
        print (u'\u001b[38;5;' + e ["color"] + 'm' +
                "{month:>2}/{day:<2} {time:<5} {name:.>30}".format (
                    month = e ["month"],
                    day   = e ["day"],
                    time  = __hour_to_time (e ["hour"]),
                    name  = e ["name"] )
                + u'\u001b[0m')

    return 0

def print_week_all ():
    TIME_INFO = tc_time.get_time_info ()
    DATA = tc_data.DATA
    summary_defaults = tc_handler.summarize_defaults (DATA, TIME_INFO)
    summary_todos = tc_handler.summarize_todos (DATA, TIME_INFO)

    to_be_done = [e for e in summary_todos if e ["done"] == "no"]
    the_rest = [e for e in summary_todos if e ["done"] == "yes"] + summary_defaults

    summary = tc_handler.sort (to_be_done) + tc_handler.sort (the_rest)

    for e in summary:
        print (u'\u001b[38;5;' + e ["color"] + 'm' +
                "{month:>2}/{day:<2} {time:<5} {name:.>30}".format (
                    month = e ["month"],
                    day   = e ["day"],
                    time  = __hour_to_time (e ["hour"]),
                    name  = e ["name"] )
                + u'\u001b[0m')

    return 0

