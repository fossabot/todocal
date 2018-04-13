# TodoCal Handle Calendar Display
# -------------------------------
# Display handler creates string list for print module to display.

from tc_print import pass_info
import tc_meta

def __get_dimension_info (raw_info):
    try:
        cell_width = int (raw_info ["cell-width"])
    except:
        try:
            cell_width = int (raw_info ["max-width"]) // 8
        except:
            tc_meta.raise_ERROR ("Error: calendar dimensions not well defined.")
