# TodoCal Data Structure in Python
# --------------------------------
# Catelog
# get_DATA: returns (dictionary object)
# parse_DATA: extract data from file and parse dictionary object (unimplemented)

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

