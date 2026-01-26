"""
SDEV 220 Module 1
Steve Kepler
25 January 2026
"""

# Practice 4.1
song = """When an eel grabs your arm,
   And it causes great harm,
   That's - a moray!"""
song = song.replace(" m", " M")
print(f"{song}\n")

# Practice 4.2
start_strings = ["My kitty cat likes",
                 "My kitty cat likes",
                 "My kitty cat fell on his",
                 "And now thinks he's a"
                 ]
end_strings = ["roast beef", "ham", "head", "clam"]

for idx in range(len(end_strings)):
    print(f"{start_strings[idx]} {end_strings[idx]}")
print()

# Practice 4.3 / 4.4
salutation = "valued customer"
name = "Jim Jones"
product = "Kroger brand equine burgers"
verbed = "spoiled"
room = "kitchen"
animals = "horses"
amount = 5
percent = 0.4
spokesman = "Robert Stump"
job_title = "VP of Customer Relations"

letter = f"""
Dear {salutation} {name},

Thank you for your letter.  We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, expecially near any {animals}.

Send us yor receipt and ${amount:.2f} for shipping anbd handling.
We will send you another {product} that, in our tests,
is {percent:.1%} less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
"""

print(letter)

# Practice 4.5
winners = ["duck", "gourd", "spitz"]

print("Congratulations to the following winners:")
for idx in range(len(winners)):
    print(f" - {winners[idx]}y Mc{winners[idx]}face".title())
print()