# def greet():
#     friend = yield #friend is equal to "suspend the function"
#     print(f"hello {friend}")
#
# g = greet()
# g.send(None) #priming the generator - runs it right before yield
# g.send("Dzikpik")
# #==hello Dzikpik
# Traceback (most recent call last):
#   File "Z:\Users\Alex\PycharmProjects\pythonStart0923\section 13 async development\9 receiving data from yield.py", line 7, in <module>
#     g.send("Dzikpik")
# StopIteration

from collections import deque
friends = deque(("Rolf","Jose","Charlie","Jen","Anna"))
def friend_upper(): #this is a generator but since it accepts date - it's called co-routine !!! ?MEGA IMPTRASOPDASD
    while friends:
            friend = friends.popleft().upper() #upper registry of the leftest
            greeting = yield
            print(f"{greeting} {friend}")

def greet(g):
    g.send(None) #priming the generator
    while True:
        try:
            greeting = yield
            g.send(greeting)
        except StopIteration:
            print("It's Joever, Anakin!")
            quit()
    #or we can "yield from g" instead of all code inside "greet(g)" but no one likes it due to complexity in reading

greeter = greet(friend_upper()) #also generator
greeter.send(None) #move the generator up to before "yield"
greeter.send("Hello there")
print("Hello world, multitasking") #to display that code runs line by line even having multiple generators and yields
greeter.send("General Kenobi 1!")
greeter.send("General Kenobi 2!")
greeter.send("General Kenobi 3!")
greeter.send("General Kenobi 4!")
