# TodoCal Event Handler

# filtering : exclude events outside of current week span
# convertion : convert all into no-repeat default or todo events

# start <= target <= end
def in_range (target, start, end):
    if target < start:
        return False
    if target > end:
        return False
    return True

def import_yearly_default (DATA, TIME_INFO):
    yearly_defaults = DATA ["events"] ["yearly"] ["default"] # un-filtered, un-converted

    filtered = []
    for event in yearly_defaults:
        event_month = int (event ["month"])
        event_day = int (event ["day"])
