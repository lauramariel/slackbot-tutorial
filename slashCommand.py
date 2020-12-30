from random import seed
from random import randint

# basic starter code for a class that can be expanded to handle callbacks, attachents (buttons, etc) and more!
class Slash():

  def __init__(self):
    self.msg = str()

  def getMessage(self):
    office_quotes=["The Dunder Mifflin stock symbol is D.M.I. Do you know what that stands for? Dummies, Morons, and Idiots. Because that’s what you’d have to be to own it. And as one of those idiots, I believe the board owes me answers.",
                    "I’m glad Michael’s getting help. He has a lot of issues, and he’s stupid.",
                    "If I don’t have some cake soon, I might die.",
                    "Identity theft is not a joke, Jim! Millions of families suffer every year.",
                    "Today, smoking is going to save lives."
                    ]
    print(f"Selecting random office quote.... ")
    random_office_quote = office_quotes[randint(0,(len(office_quotes)-1))]
    return random_office_quote
