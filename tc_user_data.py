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
            mark = tc_meta.check_mark if e ["done"] == "yes" else tc_meta.cross_mark
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
            RET [i] = tc_meta.color_white + RET [i] + tc_meta.color_reset
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
        mark = tc_meta.check_mark if e ["done"] == "yes" else tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2} {mark_s}".format (e_name = e ["name"],
                    e_month = e ["month"], e_day = e ["day"], mark_s = mark))

    # list monthly events
    RET.append ("{key_str:-^50}".format (key_str = "monthly"))
    for e in E_DICT ["monthly"] ["default"]:
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2}".format (e_name = e ["name"], e_month = '--', e_day = e ["day"]))
    for e in E_DICT ["monthly"] ["todo"]:
        mark = tc_meta.check_mark if e ["done"] == "yes" else tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2} {mark_s}".format (e_name = e ["name"],
                    e_month = '--', e_day = e ["day"], mark_s = mark))

    # list weekly events
    RET.append ("{key_str:-^50}".format (key_str = "weekly"))
    WD = { 0 : "Sun",
           1 : "Mon",
           2 : "Tue",
           3 : "Wed",
           4 : "Thur",
           5 : "Fri",
           6 : "Sat" }
    for e in E_DICT ["weekly"] ["default"]:
        RET.append ("* {e_name:<30} {e_weekday:<4}".format (e_name = e ["name"], e_weekday = WD [int (e ["day"])]))
    for e in E_DICT ["weekly"] ["todo"]:
        mark = tc_meta.check_mark if e ["done"] == "yes" else tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_weekday:<4} {mark_s}".format (e_name = e ["name"],
                    e_weekday = WD [int (e ["day"])], mark_s = mark))

    # list daily events
    RET.append ("{key_str:-^50}".format (key_str = "daily"))
    def make_hour_str (hour): # raw hour string from DATA object
        hm_l = [s.strip() for s in hour.split (' ')]
        if len(hm_l) == 1:
            return "{h:>2}:{m:<2}".format (h = hm_l[0], m = "00")
        else:
            return "{h:>2}:{m:0<2}".format (h = hm_l[0], m = hm_l[1])
    for e in E_DICT ["daily"] ["default"]:
        RET.append ("* {e_name:<30} {e_time}".format (e_name = e ["name"], e_time = make_hour_str (e ["hour"])))
    for e in E_DICT ["daily"] ["todo"]:
        mark = tc_meta.check_mark if e ["done"] == "yes" else tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_time} {mark_s}".format (e_name = e ["name"],
                    e_time = make_hour_str (e ["hour"]), mark_s = mark))

    # list no-repeat events
    RET.append ("{key_str:-^50}".format (key_str = "no-repeat"))
    for e in E_DICT ["no-repeat"] ["default"]:
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2} {e_time}".format (e_name = e ["name"],
                    e_month = e ["month"], e_day = e ["day"], e_time = make_hour_str (e ["hour"])))
    for e in E_DICT ["no-repeat"] ["todo"]:
        mark = tc_meta.check_mark if e ["done"] == "yes" else tc_meta.cross_mark
        RET.append ("* {e_name:<30} {e_month:>2}/{e_day:<2} {e_time} {mark_s}".format (e_name = e ["name"],
                    e_month = e ["month"], e_day = e ["day"], e_time = make_hour_str (e ["hour"]), mark_s = mark))

    counter = 0
    for i in range (len (RET)):
        if RET [i][0] != '-':
            counter += 1
            RET [i] = ("[{count:0>2}] ".format (count = str (counter))) + RET [i]
        else:
            RET [i] = tc_meta.color_white + RET [i] + tc_meta.color_reset
    return RET

