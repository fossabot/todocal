# TodoCal Data Handler (External)
# -------------------------------
# Catelog
# - tcl_list_min
# - tcl_list_all
# - tcl_add
# - tcl_del
# - tcl_update

from tc_data import get_DATA
import tc_meta

def tcl_list_min ():
    DATA = get_DATA () # return standard dictionary object DATA
    E_DICT = DATA ["events"] # extract event dictionary
    RET = [] # return string list

    def list_events (key): # key in yearly, monthly, weekly, daily, no-repeat
        DEFAULTS = E_DICT [key] ["default"]
        TODOS    = E_DICT [key] ["todo"]

        RET.append ("{key_str:-^35}".format (key_str = key))
        for e in DEFAULTS:
            RET.append ("* {e_name:<30}".format (e_name = e ["name"]))
        for e in TODOS:
            if e ["done"] == "yes":
                mark = tc_meta.check_mark
            else:
                mark = tc_meta.cross_mark
            RET.append ("* {e_name:<30} {mark_s}".format (e_name = e ["name"], mark_s = mark))
        return 0

    for key in ["yearly", "monthly", "weekly", "daily", "no-repeat"]:
        list_events (key)

    counter = 0
    for i in range (len (RET)):
        if RET [i][0] != '-':
            counter += 1
            RET [i] = ("[{count:0>2}] ".format (count = str (counter))) + RET [i]
        else:
            RET [i] = '\u001b[37m' + RET [i] + '\u001b[0m'
    return RET

def tcl_list_all ():
    DATA = get_DATA () # return standard dictionary object DATA
    E_DICT = DATA ["events"] # extract event dictionary
    RET = [] # return string list

    # list yearly events
    RET.append ("{key_str:-^50}".format (key_str = "yearly"))
    for e in E_DICT ["yearly"] ["default"]:
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2}".format (e_name = e ["name"], e_month = e ["month"], e_day = e ["day"]))
    for e in E_DICT ["yearly"] ["todo"]:
        if e ["done"] == "yes":
            mark = tc_meta.check_mark
        else:
            mark = tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2} {mark_s}".format (e_name = e ["name"],
                    e_month = e ["month"], e_day = e ["day"], mark_s = mark))

    # list monthly events
    RET.append ("{key_str:-^50}".format (key_str = "monthly"))
    for e in E_DICT ["monthly"] ["default"]:
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2}".format (e_name = e ["name"], e_month = '--', e_day = e ["day"]))
    for e in E_DICT ["monthly"] ["todo"]:
        if e ["done"] == "yes":
            mark = tc_meta.check_mark
        else:
            mark = tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2} {mark_s}".format (e_name = e ["name"],
                    e_month = '--', e_day = e ["day"], mark_s = mark))

    counter = 0
    for i in range (len (RET)):
        if RET [i][0] != '-':
            counter += 1
            RET [i] = ("[{count:0>2}] ".format (count = str (counter))) + RET [i]
        else:
            RET [i] = '\u001b[37m' + RET [i] + '\u001b[0m'
    return RET

