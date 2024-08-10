#atomic operation - is the one that cannot be interrupted in the middle of it. f.e. print(); deque.append() etc
from threading import  Thread
import time
import random
counter=0

def increment_counter():
    global counter
    time.sleep(random.random()) #fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
    counter +=1
    time.sleep(random.random())
    print(f"New counter value: {counter}")
    time.sleep(random.random())
    print("----------")

for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()


#with fizzying we see that previously quick threads which were executed one by one - are now partially simultaneous
# output
# New counter value: 3
# New counter value: 3
# ----------
# ----------

#once more - don't use threads if expecting to run operations sequentially