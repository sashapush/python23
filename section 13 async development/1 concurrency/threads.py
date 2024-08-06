import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor #creates a pool of threads, a bunch of threads with no target
def ask_user():
    start = time.time()
    user_input = input ("Enter name: ") #this is a blocking operation, where thread is blocked, waiting for input to happen
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user, {time.time() - start}")

def complex_calc():
    start = time.time()
    print("Started calculating..")
    [x**2 for x in range(200000000)]
    print(f"complex_calc, {time.time() - start}")

start = time.time()
ask_user()
complex_calc()
print(f"Single Thread total time, {time.time() - start}")
#before threads ask_user, 2.365781545639038
# Started calculating..
# complex_calc, 1.0608680248260498
# Single Thread total time, 3.426649570465088
print(f"Two threads total time = {time.time()-start}")

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calc)
    pool.submit(ask_user)


# Comnmented to use concurrent.futures above
# thread1 = Thread(target=complex_calc) #function, not the result, that's why no ()
# #thread2 = Thread(target=complex_calc) if we use this thread - and thread1 - there will be no time saving, and will take more time than execution complex_calc wo threads
# thread2 = Thread(target=ask_user())
#
# start=time.time()
# thread1.start()
# thread2.start()
#
# thread1.join() #tells main thread with code above to wait for thread1 to finish; it's blocking operation
# thread2.join() #same for thread2;it's blocking operation

#Two threads total time = 1.3734760284423828



