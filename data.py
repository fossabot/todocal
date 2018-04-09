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
                "yearly"    : "green red",
                "monthly"   : "green red",
                "weekly"    : "green orange",
                "daily"     : "green blue",
                "no-repeat" : "green pink",
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
                    {"name" : "Test Year 2", "month" : "4", "day" : "15", "whole-day" : "yes", "hour" : "", "length" : ""},
                    ],
                },
            "monthly" : {
                "default" : [
                    {"name" : "Test Month 1" , "day" : "12" , "whole-day" : "yes" , "hour" : ""   , "length" : ""},
                    {"name" : "Test Month 2" , "day" : "20" , "whole-day" : "no"  , "hour" : "14" , "length" : "30"},
                    ],
                "todo" : [
                    {"name" : "Test Month 3", "day" : "15", "whole-day" : "yes", "hour" : "", "length" : ""},
                    ],
                },
            "weekly" : {
                "default" : [
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

