'''
module_2_6_1.py

Steve Kepler
SDEV220
08 February 2026
Conditional practice

User inputs two integers, "secret" and "guess".  The program then compares the two and 
outputs an appropriate message
'''

while True:
    secret = input("Enter secret integer between 1 and 10, inclusive: ")
    try:
        secret = int(secret)
        break
    except ValueError:
        print("Secret number must be an integer between 1 and 10, inclusive.")


while True:
    guess = input("Enter guess between 1 and 10, inclusive: ")
    try:
        guess = int(guess)
        break
    except ValueError:
        print("Guess must be an integer between 1 and 10, inclusive.")

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")