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

