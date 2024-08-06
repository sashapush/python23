import time
from multiprocessing import Process
def ask_user():
    start = time.time()
    user_input = input ("Enter name: ") #this is a blocking operation, where thread is blocked, waiting for input to happen
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user, {time.time() - start}")

def complex_calc():
    start = time.time()
    print("Started calculating..")
    [x**2 for x in range(100000000)]
    print(f"complex_calc, {time.time() - start}")



#Processes
if __name__ == "__main__":
    start = time.time()
    ask_user()
    complex_calc()
    print(f"Single Thread total time, {time.time() - start}")

    process = Process(target=complex_calc)
    process2 = Process(target=complex_calc)
    process.start()
    process2.start()
    start = time.time()
    process.join()  # wait until process finishes
    process2.join()  # wait until process finishes
    print(f"Two process total time, {time.time() - start}")
