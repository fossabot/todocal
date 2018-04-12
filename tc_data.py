# TodoCal Data Structure in Python
# --------------------------------
# Catelog
# DATA (dictionary object)

DATA = {
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
                "max-height" : "35",
                },
            },
        "events" : {
            "yearly" : {
                "default" : [
                    {"name" : "My Birthday" , "month" : "11" , "day" : "30" , "whole-day" : "yes" , "hour" : ""   , "length" : ""},
                    {"name" : "Test Year 1" , "month" : "4"  , "day" : "1"  , "whole-day" : "no"  , "hour" : "10" , "length" : "120"},
                    ],
                "todo" : [
                    {"name" : "Test Year 2", "month" : "4", "day" : "15", "whole-day" : "yes",
                                            "hour" : "", "length" : "", "done" : "no"}, # current year instance
                    ],
                },
            "monthly" : {
                "default" : [
                    {"name" : "Test Month 1" , "day" : "12" , "whole-day" : "yes" , "hour" : ""   , "length" : ""},
                    {"name" : "Test Month 2" , "day" : "20" , "whole-day" : "no"  , "hour" : "14" , "length" : "30"},
                    ],
                "todo" : [ # current month instance
                    {"name" : "Test Month 3", "day" : "15", "whole-day" : "yes", "hour" : "", "length" : "", "done" : "no"},
                    {"name" : "Test Month 4", "day" : "15", "whole-day" : "yes", "hour" : "", "length" : "", "done" : "yes"},
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
                    {"name" : "Test Week 1" , "day" : "0" , "hour" : "16" , "length" : "180" , "done" : "yes"} ,
                    {"name" : "Test Week 2" , "day" : "3" , "hour" : "16" , "length" : "100" , "done" : "no"}  ,
                    {"name" : "Test Week 3" , "day" : "1" , "hour" : "8"  , "length" : "30"  , "done" : "no"}  ,
                    ],
                },
            "daily" : {
                "default" : [
                    ],
                "todo" : [ # weekly instances by day
                    {"name" : "Test Day 1" , "hour" : "11 30" , "length" : "20" , "done" : "0 1 4 6"} ,
                    {"name" : "Test Day 2" , "hour" : "20 40" , "length" : "50" , "done" : "1 2 3"}   ,
                    ],
                },
            "no-repeat" : {
                "default" : [
                    {"name" : "Test NoRep 1" , "month" : "4" , "day" : "19" , "hour" : "9 30" , "length" : "15"}  ,
                    {"name" : "Test NoRep 2" , "month" : "5" , "day" : "1"  , "hour" : "21"   , "length" : "150"} ,
                    ],
                "todo" : [
                    {"name" : "Test NoRep 3" , "month" : "4" , "day" : "19" , "hour" : "10"    , "length" : "20" , "done" : "no"}  ,
                    {"name" : "Test NoRep 4" , "month" : "4" , "day" : "7"  , "hour" : "15 20" , "length" : "30" , "done" : "yes"} ,
                    {"name" : "Test NoRep 5" , "month" : "4" , "day" : "5"  , "hour" : "17 15" , "length" : "45" , "done" : "no"}  ,
                    ],
                },
            },
        }

