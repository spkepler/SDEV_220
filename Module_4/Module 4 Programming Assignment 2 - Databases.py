'''
Module 4 Programming Assignment 2 - Databases.py

Chapter 23 Exercises

Steve Kepler
10 March 2026
'''

# Exercise 23-1:  Saving to a CSV file
import csv
print("\nExercise 23-1:  Saving to a CSV file\n")
book_data = [
    ['author', 'book'],
    ['J R R Tolkien', 'The Hobbit'],
    ['Lynn Truss', '"Eats, Shoots, & Leaves"']
]
with open('books.csv', 'wt', newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(book_data)


# Exercise 23-2:  Using DictReader()
print("Exercise 23-2:  Using DictReader()\n")
with open('books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(f'{books}\n')
'''Note:  DictReader handled the commas in the Lynn Truss record with no problems.'''


# Exercise 23-3:  Creating second CSV File
print("\nExercise 23-3:  Creating second CSV file\n")
book_data = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],
    ['Perdido Street Station', 'Chine Miéville', '2000'],
    ['Thud!', 'Terry Pratchett', '2005'],
    ['The Spellman Files', 'Lisa Lutz', '2007'],
    ['Small Gods', 'Terry Pratchett', '1992']
]
with open('books2.csv', 'wt', newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(book_data)

# Exercise 23-4:  Create SQLite database
print("\nExercise 23-4:  Create SQLite database")
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
            (title VARCHAR(30) PRIMARY KEY,
             author VARCHAR(30),
             year INT)''')
curs.close()
conn.close()

# Exercise 23-5:  Read file and insert into SQLite database
print('\nExercise 23-5:  Read file and insert into SQLite database')
with open('books2.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    book_data = [row for row in cin]

conn = sqlite3.connect('books.db')
curs = conn.cursor()
ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'

for book in book_data:
    curs.execute(ins, (book.get('title'), book.get('author'), book.get('year')))

conn.commit()
curs.close()
conn.close()


# Exercise 23-6:  Read SQLite database and print titles
print('\nExercise 23-6:  Read SQLite database and print titles')

conn = sqlite3.connect('books.db')
curs = conn.cursor()

curs.execute('SELECT title FROM books ORDER BY title')
titles = curs.fetchall()

curs.close()
conn.close()

print(titles)


# Exercise 23-7:  Read SQLite database and print all, sorted by year
print('\nExercise 23-6:  Read SQLite database and print all, sorted by year')

conn = sqlite3.connect('books.db')
curs = conn.cursor()

curs.execute('SELECT * FROM books ORDER BY year')
titles = curs.fetchall()

curs.close()
conn.close()

print(titles)