'''
module_3_hwk_ch_10.py

Steve Kepler
SDEV220
16 February 2026
Functions


'''

# Problem 10-1
def good():
    return ['Harry', 'Ron', 'Hermione']


# Problem 10-2
def get_odds():
    return [num for num in range(10) if num % 2 == 1]

odds = get_odds()
for idx in range(len(odds)):
    if idx == 2:
        print(odds[idx])


# Problem 10-3
def my_decorator(func):
    def new_function(*args,**kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return new_function
    
@my_decorator
def my_func():
    print("This is my function.")

my_func()

# Problem 10-4
class OopsException(Exception):
    pass

try:
    raise OopsException('Caught and oops.')
except OopsException as exc:
    print(exc)