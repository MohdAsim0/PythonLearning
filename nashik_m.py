
from random import choice


capital = "Upnagar"
bird = "Peacock"
flower = "Rose"


def random_facts():
    funfacts = [
        'Nashik is a beautiful city',
        "Wichita is the largest city in the state, but many guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")
    print(funfacts[int(index)])


if __name__ == "__main__":
    random_facts()
# this line runs if we run this nashik_m.py file
# But if we import this as module in other file it will not run directly
