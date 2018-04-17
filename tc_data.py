# TodoCal Data Structure in Python
# --------------------------------
# Catelog
# get_DATA: returns (dictionary object)
# parse_DATA: extract data from file and parse dictionary object (unimplemented)

__base_path = "user-path/"

def __parse_files ():
    f_settings = open (__base_path + ".todocalrc", 'r')
    data_path = __base_path + ".todocal/"
    f_colorcode = open (data_path + "color-code", 'r' )
    f_yearly =    open (data_path + "yearly",     'r' )
    f_monthly =   open (data_path + "monthly",    'r' )
    f_weekly =    open (data_path + "weekly",     'r' )
    f_daily =     open (data_path + "daily",      'r' )
    f_norepeat =  open (data_path + "no-repeat",  'r' )

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

def parse_DATA ():
    pass

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

