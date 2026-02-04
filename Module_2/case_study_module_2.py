'''
case_study_module_2.py

Steve Kepler
SDEV220
04 February 2026
Case Study Module 2: if ... else and while

This module prompts the user for a student's last name, first name, and
GPA.  The loop repeats until 'ZZZ' is entered for the last name.  If a
non-numeric value is entered for the GPA, an error message is give and the 
user re-prompted to enter a valid GPA.
'''

while ((last_name := input("Input last name, or 'ZZZ' to quit: ")) != "ZZZ"):
    first_name = input("Input first name: ")
    while True:
        gpa = input("Input GPA: ")
        try:
            gpa = float(gpa)
            break
        except ValueError:
            print("GPA must me a numeric value.")

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")