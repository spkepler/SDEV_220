'''
Module 4 Programming Assignment 1 - Files and Text Files.py

Chapter 17 and Chapter 20 Exercises

Steve Kepler
08 March 2026
'''

# Exercise 17-4

mammoth = '''
    We have seen the Queen of cheese,
        Laying quietly at your ease,
        Gently fanned by evening breeze —
        Thy fair form no flies dare seize.

        All gaily dressed soon you'll go
        To the great Provincial Show,
        To be admired by many a beau
        In the city of Toronto.

        Cows numerous as a swarm of bees —
    Or as the leaves upon the trees —
    It did require to make thee please,
    And stand unrivalled Queen of Cheese.

    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great World's show at Paris.

    Of the youth — beware of these —
    For some of them might rudely squeeze
    And bite your cheek; then songs or glees
    We could not sing o' Queen of Cheese.

    We'rt thou suspended from baloon,
    You'd cast a shade, even at noon;
    Folks would think it was the moon
    About to fall and crush them soon.
    '''

# Exercise 17-5:  Find all words beginning with 'c'
print('\n*** Exercise 17-5 ***')
import re
c_words = re.findall(r'\b[cC]\w*', mammoth)
print(c_words)

# Exercise 17-6:  Find 4-Letter word beginning with 'c'
print('\n*** Exercise 17-6 ***')
four_letter_words = [c_word for c_word in c_words if len(c_word) == 4]
print(four_letter_words)

# Exercise 17-7:  Find all words that end with 'r'
print('\n*** Exercise 17-7 ***')
r_words = re.findall(r'\b\w*[rR]\b', mammoth)
print(r_words)

# Exercise 17-8:  Findall words that contain exactly 3 vowels in a row
print('\n*** Exercise 17-8 ***')
v_words =re.findall(r'\b\w*[aeiouAEIOU]{3}\w*\b', mammoth)
print(v_words)

# Exercise 20-1:  List all files in current directory
import os
print('\n*** Exercise 20-1 ***')
contents = os.listdir('.')
print('Directory Contents')
for content in contents:
    print(f'\t{content}')

# Exercise 20-2:  List all files in parent directory
print('\n*** Exercise 20-2 ***')
contents = os.listdir('..')
print('Parent Directory Contents')
for content in contents:
    print(f'\t{content}')

# Exercise 20-3:  Create text file
print('\n*** Exercise 20-3 ***')
test1 = "This is a test of the emergency text system"
with open('test.txt','w') as f:
    f.write(test1)

# Exercise 20-4:  Verify contents of file.txt
print('\n*** Exercise 20-4 ***')
with open('test.txt', 'r') as f:
    test2 = f.read()

print(f'Test 1: {test1}')
print(f'Test 2: {test2}')
if test1 == test2:
    print("They are the same\n")
else:
    print("They are different\n")

'''Note that you get different results in 20-4 with readlines() instead of read()
   This is because readlines returns a list of strings versus a single string'''