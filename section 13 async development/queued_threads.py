#goal is to display logic of queuing of threads with shared state
#when threads work with shared stated - queues are needed
import  time
import random
import queue
from threading import  Thread #later to ThreadPoolExecutor

counter = 0
job_queue = queue.Queue() #things to be printed out
counter_queue = queue.Queue() #amounts by which to increadse counter

def increment_manager():
    global counter # stating that variable in local scope = variable in global scope
    while True:
        increment = counter_queue.get() #this waits until and item is available and then locks the queue
        time.sleep(
            random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
        old_counter = counter
        time.sleep(
            random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
        counter = old_counter + increment
        time.sleep(
            random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
        job_queue.put((f"New counter value is {counter}", "-----")) #tuple needs to be put in the queue
        time.sleep(
            random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
        counter_queue.task_done() #this unlocks the queue so that another thread can use counter_queue()

Thread(target=increment_manager, daemon=True).start() #daemon = True means that will run forever unless error is observed.

def printer_manager():
    while True:
        for line in job_queue.get(): #this also lock the queue and waits for an item to be available
            print(line)
            time.sleep(
                random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
        job_queue.task_done()#this unlocks the queue so that another thread can use job_queue()

Thread(target=printer_manager, daemon=True).start() #daemon = True means that will run forever unless error is observed.

##and somehow we need to increase the counter.
def increment_counter():
    counter_queue.put(1)
    time.sleep(
        random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps

worker_threads = [Thread(target=increment_counter) for thread in range(10)]
#start the threads above
for thread in worker_threads:
    time.sleep(
        random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
    thread.start()
#wait for threads to finish
for thread in worker_threads:
    time.sleep(
        random.random())  # fizzying tecnhique - putting time.sleep random after every line of code for multithreaded apps
    thread.join()
#and wait for counter_queue to finish, so that nothing is left in the queue
counter_queue.join()
#and wait for job_queue to finish
job_queue.join()