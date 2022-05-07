import random
import layout
import fonts

top = layout.bottom+layout.margin*2+24

love = [
    {
        "lines": [
            "",
            "Thank you for everything",
            "",
    ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "buying me toys",
            "",
            ""
        ],
        "from":"Joe"
    },
        {
        "lines": [
            "I love you!",
            "",
            "",
            ""
        ],
        "from":"Joe"
    },        {
        "lines": [
            "I love you!",
            "",
            "",
            ""
        ],
        "from":"Andreas"
    },     
       {
        "lines": [
            "Thank you for taking",
            "care of me when I",
            "am sick",
            ""
        ],
        "from":"Andreas"
    },
]


def draw_love(draw):
    saying = random.choice(love)
    width = 400-layout.margin*2
    layout.draw_centered(draw,saying["lines"][0],fonts.sayings,top,layout.margin,width)
    layout.draw_centered(draw,saying["lines"][1],fonts.sayings,top+24,layout.margin,width)
    layout.draw_centered(draw,saying["lines"][2],fonts.sayings,top+48,layout.margin,width)
    layout.draw_centered(draw,saying["lines"][3],fonts.sayings,top+72,layout.margin,width)
    layout.draw_centered(draw,"--" +saying["from"],fonts.small,top+120,200,100)

