#continues from #9
from collections import deque
from types import coroutine
friends = deque(("Rolf","Jose","Charlie","Jen","Anna"))

@coroutine
def friend_upper(): #this is a generator but since it accepts date - it's called co-routine !!! ?MEGA IMPTRASOPDASD
    while friends:
            friend = friends.popleft().upper() #upper registry of the leftest
            greeting = yield
            print(f"{greeting} {friend}")

async def greet(g):
    print("Starting")
    await g
    print("Ending") #will be printed once coroutine is empty
    # g.send(None) #priming the generator
    # while True:
    #     try:
    #         greeting = yield
    #         g.send(greeting)
    #     except StopIteration:
    #         print("It's Joever, Anakin!")
    #         quit()
    #or we can "yield from g" instead of all code inside "greet(g)" but no one likes it due to complexity in reading
##AS FOR STOPITERATION EXCEPTION
#you should catch this in the main script. But really, StopIteration is used internally by Python to signal e.g. the end of a for loop. Oftentimes you won't have to catch it yourself.
greeter = greet(friend_upper()) #also generator
greeter.send(None) #move the generator up to before "yield"
greeter.send("Hello there")
print("Hello world, multitasking") #to display that code runs line by line even having multiple generators and yields
greeter.send("General Kenobi 1!")
greeter.send("General Kenobi 2!")
greeter.send("General Kenobi 3!")

greeting = input("Type greeting here")
greeter.send(greeting)
