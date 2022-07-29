def say_hello():
    print('hello!')

say_hello()


#parameters and arguments

def say_hello(name, age):
    print(f'hello! {name}, you are {age} years old')

say_hello('ade', 15)

#positional argument
def say_hello(name, age):
    print(f'hello! {name}, you are {age} years old')

say_hello(15, 'ade')#the order of the parameters should be followed, otherwise it prints the way its position when function is called

#keyword argument
def say_hello(name, age):
    print(f'hello! {name}, you are {age} years old')

say_hello(name = 'Kay', age = 15)#the keyword arguments takes priority

#default parameters
def say_hello(name = 'Nelson', age = 20): #when no argument is given when function is called, it defaults to the default param
    print(f'hello! {name}, you are {age} years old')

say_hello()