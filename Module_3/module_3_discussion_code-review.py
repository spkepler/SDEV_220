'''
module_3_discussion_code_review.py

Steve Kepler
SDEV220
11 February 2026
Creating class definitions

The User class contains several relevant pieces of information for each
user.  Standard parameters are first name, last name, title, occupation, and 
address city and state.  Additional arguments can be passed as "fun facts".
'''

from datetime import datetime

class User:
    def __init__(self, first_name, last_name, title, occupation, addr_city, addr_state, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.occupation = occupation
        self.addr_city = addr_city
        self.addr_state = addr_state
        self.fun_facts = kwargs

    def describe_user(self):
        print(f"\nInformation on {self.title} {self.first_name} {self.last_name}:")
        print(f"\tOccupation: {self.occupation}")
        print(f"\tResides in {self.addr_city}, {self.addr_state}")
        if self.fun_facts:
            print(f"\tSome fun facts about {self.first_name}:")
            for key, value in self.fun_facts.items():
                print(f"\t  {key} - {value}")
        
    def greet_user(self, formal=True):

        if formal:
            t = datetime.now().hour

            if t < 12:
                time_of_day = "morning" 
            elif t < 16:
                time_of_day = "afternoon"
            elif t < 18:
                time_of_day = "prevening"
            elif t < 22:
                time_of_day = "evening"
            else:
                time_of_day = "night"

            print(f"Good {time_of_day}, {self.title} {self.last_name}.")
        else:
            print(f"Hey, {self.first_name}.")

characters = [
    {"first_name": "Sheldon",
     "last_name":"Cooper",
     "title":"Dr.",
     "occupation": "theoretical physicist",
     "addr_city": "Pasadena",
     "addr_state": "California",
     "Siblings":"George, Missy",
     "Awards":"Nobel Prize"
     },
     {"first_name": "Leonard",
     "last_name":"Hofstadter",
     "title":"Dr.",
     "occupation": "theoretical physicist",
     "addr_city": "Pasadena",
     "addr_state": "California",
     "Love Interests": "Penny, Priya Koothrappali, Dr. Stephanie Barnett, Leslie Winkle, Joyce Kim",
     "Felonies": "Blew up elevator trying to impress Joyce Kim, but never charged"        
     },
     {"first_name": "Howard",
     "last_name":"Wolowitz",
     "title":"Mr.",
     "occupation": "engineer",
     "addr_city": "Pasadena",
     "addr_state": "California", 
     "Other Occupations": "astronaut"       
     },
     {"first_name": "Penny",
     "last_name":"Hofstadter",
     "title":"Mrs.",
     "occupation": "waitress",
     "addr_city": "Pasadena",
     "addr_state": "California",
     "Other Occupatons": "Aspiring actress"       
     },
     {"first_name": "Priya",
     "last_name":"Koothrappali",
     "title":"Ms.",
     "occupation": "attorney",
     "addr_city": "New Delhi",
     "addr_state": "India"        
     }
]

character_list = [User(**character) for character in characters]

print("\nFormal Greetings:")
for character in character_list:
    print("\t",end='')
    character.greet_user()

print("\nInformal Greetings:")
for character in character_list:
    print("\t",end='')
    character.greet_user(False)

print("\nAbout the Characters:")
for character in character_list:
    character.describe_user()

print()