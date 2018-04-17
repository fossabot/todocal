# TodoCal Data Structure in Python
# --------------------------------
# Catelog
# get_DATA: returns (dictionary object)
# parse_DATA: extract data from file and parse dictionary object

import tc_meta

__base_path = "user-path/"

def __parse_files ():
    try:
        f_settings = open (__base_path + ".todocalrc", 'r')
        data_path = __base_path + ".todocal/"
        f_colorcode = open (data_path + "color-code", 'r' )
        f_yearly =    open (data_path + "yearly",     'r' )
        f_monthly =   open (data_path + "monthly",    'r' )
        f_weekly =    open (data_path + "weekly",     'r' )
        f_daily =     open (data_path + "daily",      'r' )
        f_norepeat =  open (data_path + "no-repeat",  'r' )
    except:
        tc_meta.raise_ERROR ("TodoCal: data file path invalid.")

    raw_settings  = [line.strip() for line in f_settings]
    raw_colorcode = [line.strip() for line in f_colorcode]
    raw_yearly    = [line.strip() for line in f_yearly]
    raw_monthly   = [line.strip() for line in f_monthly]
    raw_weekly    = [line.strip() for line in f_weekly]
    raw_daily     = [line.strip() for line in f_daily]
    raw_norepeat  = [line.strip() for line in f_norepeat]

    # filter out empty lines and commented lines
    filter_settings  = [s for s in raw_settings  if len(s) != 0 and s[0] != '#']
    filter_colorcode = [s for s in raw_colorcode if len(s) != 0 and s[0] != '#']
    filter_yearly    = [s for s in raw_yearly    if len(s) != 0 and s[0] != '#']
    filter_monthly   = [s for s in raw_monthly   if len(s) != 0 and s[0] != '#']
    filter_weekly    = [s for s in raw_weekly    if len(s) != 0 and s[0] != '#']
    filter_daily     = [s for s in raw_daily     if len(s) != 0 and s[0] != '#']
    filter_norepeat  = [s for s in raw_norepeat  if len(s) != 0 and s[0] != '#']

    return (filter_settings,
            filter_colorcode,
            filter_yearly,
            filter_monthly,
            filter_weekly,
            filter_daily,
            filter_norepeat)

def parse_DATA ():
    (settings, colorcode, yearly, monthly, weekly, daily, norepeat) = __parse_files ()

    DATA = {"meta" : {"color-code" : {}, "color" : {}, "dimension" : {}},
            "events" : {
                "yearly" : {"default" : [], "todo" : []},
                "monthly" : {"default" : [], "todo" : []},
                "weekly" : {"default" : [], "todo" : []},
                "daily" : {"default" : [], "todo" : []},
                "no-repeat" : {"default" : [], "todo" : []}}} # initialize DATA

    # parse settings
    try:
        color_settings_index = settings.index ("__color")
    except:
        tc_meta.raise_ERROR ("TodoCal: color settings not defined.")
    try:
        dimension_settings_index = settings.index ("__dimension")
    except:
        tc_meta.raise_ERROR ("TodoCal: dimension settings not defined.")
    for i in range(color_settings_index + 1, dimension_settings_index):
        line = settings [i]
        (key, value) = [s.strip() for s in line.split (':')]
        DATA ["meta"] ["color"] [key] = value
    for i in range(dimension_settings_index + 1, len(settings)):
        line = settings [i]
        (key, value) = [s.strip() for s in line.split (':')]
        DATA ["meta"] ["dimension"] [key] = value

    # regularized event parser
    def parse_event (line):
        if line[0] != '{' or line[-1] != '}':
            tc_meta.raise_ERROR ("TodoCal: event data storage corrupted.")
        line = line[1:-1].strip() # remove line container
        kv_pairs = [s.strip() for s in line.split (',')]
        E = {}
        for kv in kv_pairs:
            kv_l = [s.strip() for s in kv.split (':')]
            key = kv_l [0]
            value = kv_l [1]
            E [key] = value
        return E

    # categorize events
    def get_categorizers (L):
        try:
            default_index = L.index ("__default")
            todo_index = L.index ("__todo")
        except:
            tc_meta.raise_ERROR ("TodoCal: event data storage problem.")
        return (default_index, todo_index)
    y_indices = get_categorizers (yearly)
    m_indices = get_categorizers (monthly)
    w_indices = get_categorizers (weekly)
    d_indices = get_categorizers (daily)
    n_indices = get_categorizers (norepeat)
    (yearly_default, yearly_todo) = (yearly[y_indices[0] + 1 : y_indices], yearly[y_indices[1] + 1:len(yearly)])
    (monthly_default, monthly_todo) = (monthly[m_indices[0] + 1 : m_indices], monthly[m_indices[1] + 1:len(monthly)])
    (weekly_default, weekly_todo) = (weekly[w_indices[0] + 1 : w_indices], weekly[w_indices[1] + 1:len(weekly)])
    (daily_default, daily_todo) = (daily[d_indices[0] + 1 : d_indices], daily[d_indices[1] + 1:len(daily)])
    (norepeat_default, norepeat_todo) = (norepeat[n_indices[0] + 1 : n_indices], norepeat[n_indices[1] + 1:len(norepeat)])

    # parse events and update DATA
    DATA ["events"] ["yearly"] ["default"]   = [parse_event (line) for line in yearly_default]
    DATA ["events"] ["monthly"] ["default"]  = [parse_event (line) for line in monthly_default]
    DATA ["events"] ["weekly"] ["default"]   = [parse_event (line) for line in weekly_default]
    DATA ["events"] ["daily"] ["default"]    = [parse_event (line) for line in daily_default]
    DATA ["events"] ["norepeat"] ["default"] = [parse_event (line) for line in norepeat_default]
    DATA ["events"] ["yearly"] ["todo"]   = [parse_event (line) for line in yearly_todo]
    DATA ["events"] ["monthly"] ["todo"]  = [parse_event (line) for line in monthly_todo]
    DATA ["events"] ["weekly"] ["todo"]   = [parse_event (line) for line in weekly_todo]
    DATA ["events"] ["daily"] ["todo"]    = [parse_event (line) for line in daily_todo]
    DATA ["events"] ["norepeat"] ["todo"] = [parse_event (line) for line in norepeat_todo]

__DATA = {
        "meta" : {
            "color-code" : {
                "white"        : "015",
                "black"        : "016",
                "red"          : "160",
                "blue"         : "069",
                "light-blue"   : "081",
                "dark-blue"    : "057",
                "green"        : "046",
                "light-green"  : "119",
                "dark-green"   : "028",
                "yellow"       : "226",
                "pink"         : "213",
                "orange"       : "208",
                "purple"       : "129",
                "light-purple" : "141",
                "dark-purple"  : "128",
                "brown"        : "130",
                "teal"         : "108",
                "cyan"         : "087",
                "magenta"      : "165",
                },
            "color" : {
                "yearly"    : "green red orange", # default, todo, late
                "monthly"   : "green red yellow",
                "weekly"    : "green orange red",
                "daily"     : "green blue red",
                "no-repeat" : "green pink magenta",
                },
            "dimension" : {
                "cell-width" : "16",
                "max-height" : "30",
                },
            },
        "events" : {
            "yearly" : {
                "default" : [
                    {"name" : "My Birthday" , "month" : "11" , "day" : "30" , "whole-day" : "yes" , "hour" : ""   , "length" : ""},
                    ],
                "todo" : [
                    ],
                },
            "monthly" : {
                "default" : [
                    ],
                "todo" : [ # current month instance
                    ],
                },
            "weekly" : {
                "default" : [
                    {"name" : "259 Lecture"           , "day" : "1" , "hour" : "9 30"  , "length" : "50"},
                    {"name" : "Interp Session"        , "day" : "1" , "hour" : "12 30" , "length" : "50"},
                    {"name" : "StuCo Origami"         , "day" : "1" , "hour" : "18 30" , "length" : "80"},
                    {"name" : "259 Recitation"        , "day" : "2" , "hour" : "10 30" , "length" : "50"},
                    {"name" : "150 Lecture"           , "day" : "2" , "hour" : "12"    , "length" : "80"},
                    {"name" : "150 Lab"               , "day" : "3" , "hour" : "10 30" , "length" : "80"},
                    {"name" : "251 Homework Writing"  , "day" : "3" , "hour" : "18 30" , "length" : "80"},
                    {"name" : "251 Lecture"           , "day" : "4" , "hour" : "15"    , "length" : "80"},
                    {"name" : "Interp Session"        , "day" : "5" , "hour" : "12 30" , "length" : "80"},
                    {"name" : "251 Rewrite"           , "day" : "5" , "hour" : "16 30" , "length" : "50"},
                    {"name" : "251 Homework Solution" , "day" : "6" , "hour" : "12 30" , "length" : "60"},
                    {"name" : "251 Homework Solution" , "day" : "0" , "hour" : "12 30" , "length" : "60"},
                    {"name" : "251 Recitation"        , "day" : "6" , "hour" : "14 30" , "length" : "60"},
                    ],
                "todo" : [ # current week instance
                    ],
                },
            "daily" : {
                "default" : [
                    ],
                "todo" : [ # weekly instances by day
                    ],
                },
            "no-repeat" : {
                "default" : [
                    ],
                "todo" : [
                    ],
                },
            },
        }

def get_DATA ():
    return __DATA

