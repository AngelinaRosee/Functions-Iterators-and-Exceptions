def add_numbers(a, b):
    return a+b

def join_words(*args):
    return ' '.join(args)

def rec_countdown(n):
    if n==0:
         return n #Base Case
    if n<0:
        return -1 #Handling negative values
    print(n)
    return rec_countdown(n-1) #Recursive call

def greet(name):
    return "Hello" + ' ' + name 

def repeat_phrase(phrase, repetition=2):
    for i in range(repetition):
        print(phrase)

def apply_function(func, val):
    return func(val)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    finally: #Modification
        print("Division attempted")

def check_age(age):
    if age<0 or type(age)!=int:
        raise ValueError("Age must be a positive integer")
    return age

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        print("The value provided cannot be converted to an integer")

class Countdown:
    def __init__(self, start):
        self.start=start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:  #If countdown<0, stop
            raise StopIteration

        current_value = self.start
        self.start -= 1  #Decrement current val

        return current_value

import itertools

def main():

    add_lambda =lambda a,b:a+b
    join_words_lambda = lambda *args: ' '.join(args)

    print(add_numbers(3,5))
    print(add_lambda(3,5))

    print(join_words("Hello", "world", "!"))
    print(join_words_lambda("Hello", "world", "!"))

    print(rec_countdown(5))

    print(greet("Alice"))

    print(repeat_phrase("Hello"))
    print(repeat_phrase("Hello", 3))

    print(apply_function(lambda x: x.upper(), "hello"))

    print(safe_divide(5,2))
    print(safe_divide(5, 0)) #Test Case

    print(check_age(10))

    print(parse_int("12345678"))

    rand_list=[5, 4, 3, 2, 1]
    my_interator=iter(rand_list)
    print(next(my_interator))
    print(next(my_interator))
    print(next(my_interator))
    print(next(my_interator))
    print(next(my_interator))

    words=['hello', 'world', 'my', 'name', 'is', 'angelina']
    for word in words:
        print(word.upper())

    countdown=Countdown(5)
    for num in countdown:
        print(num)

    colors=["red", "blue", "green"]
    color_cycle = itertools.cycle(colors)
    for i in range(6):
        print(next(color_cycle))
main()