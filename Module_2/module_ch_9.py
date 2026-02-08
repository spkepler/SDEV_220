'''
module_ch_9.py

Steve Kepler
SDEV220
08 February 2026
Chapter 9 Practice Exercises

'''

# 9.6
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}
print()

# 9.7
print(life.keys())

# 9.8
print(life['animals'].keys())

# 9.9
print(life['animals']['cats'])

# 9.10
squares = {number:number**2 for number in range(10)}
print(squares)

# 9.11
odd = {i for i in range(10) if i % 2 == 1}
print(odd)

# 9.14
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
movies = dict(zip(titles, plots))
print(movies)