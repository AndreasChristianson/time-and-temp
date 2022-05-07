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
    {
        "lines": [
            "Thank you for",
            "getting me a house",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "buying me pets",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "life",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "buying me food",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "a family",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "help when I need it",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "Thank you for",
            "being my mom",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "I love it when you",
            "read to me at bedtime.",
            "Thank you!",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "I love how you",
            "give me hugs",
            "",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "You are sooo",
            "beautiful!",
            "",
            ""
        ],
        "from":"Andreas"
    },
    {
        "lines": [
            "You are always there",
            "when I need to talk",
            "",
            ""
        ],
        "from":"Andreas"
    },
    {
        "lines": [
            "I am always happy when",
            "when you call. I like",
            "hearing your voice;",
            "it always has a giggle"
        ],
        "from":"Andreas"
    },
    {
        "lines": [
            "Thank you for marrying me!",
            "",
            "",
            ""
        ],
        "from":"Andreas"
    },
    {
        "lines": [
            "I love how you help me",
            "when I need it, unlike",
            "dad...",
            ""
        ],
        "from":"Joe"
    },

    {
        "lines": [
            "I like how you help me",
            "do things that I",
            "could not do alone",
            ""
        ],
        "from":"Joe"
    },
    {
        "lines": [
            "I like when you punch me.",
            "Slug bug!",
            "",
            ""
        ],
        "from":"Andreas"
    },
    {
        "lines": [
            "This message good for",
            "one back rub.",
            "Take a picture for proof!",
            ""
        ],
        "from":"Andreas"
    },
    {
        "lines": [
            "Thank you for calling me out",
            "on my bullshit. I'm not always",
            "right, I just want to be.",
            ""
        ],
        "from":"Andreas"
    },
]


def draw_love(draw):
    saying = random.choice(love)
    width = 400-layout.margin*2
    layout.draw_centered(
        draw, saying["lines"][0], fonts.sayings, top, layout.margin, width)
    layout.draw_centered(
        draw, saying["lines"][1], fonts.sayings, top+24, layout.margin, width)
    layout.draw_centered(
        draw, saying["lines"][2], fonts.sayings, top+48, layout.margin, width)
    layout.draw_centered(
        draw, saying["lines"][3], fonts.sayings, top+72, layout.margin, width)
    layout.draw_centered(
        draw, "--" + saying["from"], fonts.sig, top+120, 200, 100)
