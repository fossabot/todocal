# TodoCal Handle Calendar Display
# -------------------------------
# Display handler creates string list for print module to display.

from tc_print import pass_info

def __get_dimension_info (raw_info):
    try:
        cell_width = int (raw_info ["cell-width"])
    except:
        try:
            cell_width = int (raw_info ["max-width"]) // 8
        except:
            print ('\u001b[31mUnexpected Error.\u001b[0m')
