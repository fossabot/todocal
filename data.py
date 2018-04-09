# TodoCal Data Structure in Python

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
                                            "hour" : "", "length" : "", "done" : "no"},
                    ],
                },
            "monthly" : {
                "default" : [
                    {"name" : "Test Month 1" , "day" : "12" , "whole-day" : "yes" , "hour" : ""   , "length" : ""},
                    {"name" : "Test Month 2" , "day" : "20" , "whole-day" : "no"  , "hour" : "14" , "length" : "30"},
                    ],
                "todo" : [
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
                "todo" : [
                    ],
                },
            "daily" : {
                "default" : [
                    ],
                "todo" : [
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

