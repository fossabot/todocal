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
            RET.append ("* {e_name:<30}".format (e_name = e ["name"]))
        return 0

    for key in ["yearly", "monthly", "weekly", "daily", "no-repeat"]:
        list_events (key)

    counter = 0
    for i in range (len (RET)):
        if RET [i][0] != '-':
            counter += 1
            RET [i] = ("[{count:0>3}] ".format (count = str (counter))) + RET [i]
    return RET

