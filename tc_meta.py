# TodoCal Meta Program Control
# ----------------------------
# Catelog
# raise_ERROR (msg): raise fatal error and quit program
# raise_WARNING (msg): print warning message continue program

import os.path as osp

def raise_ERROR (msg):
    if msg == "":
        msg = "TodoCal Error."
    print ('\u001b[31;1m' + msg + '\u001b[0m')
    quit()

def raise_WARNING (msg):
    if msg == "":
        msg = "TodoCal Warning."
    print ('\u001b[33;1m' + msg + '\u001b[0m')

base_path = osp.expanduser ('~') + "/"
