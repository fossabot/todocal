# TodoCal Print Functions

import tc_time
import tc_data
import tc_handler

def print_week_defaults ():
    TIME_INFO = tc_time.get_time_info ()
    DATA = tc_data.DATA
    summary = tc_handler.summarize_defaults (DATA, TIME_INFO)
