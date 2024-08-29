# it's as if threading, but less efficient lul
def countdown(n):  # still a generator
    while n > 0:
        yield n  # at this point command is suspended
        n -= 1


# c1 = countdown(10)
# c2 = countdown(20)
# print(next(c1))
# print(next(c2))
# print(next(c1))
# print(next(c2))
# 2 tasks yielding control of the main thread to one another
# print(next(c))  # 10
# print(next(c))  # 9
# print(next(c))  # 8
# _______________________________________________________
# next step - create a set of tasks

tasks = [countdown(10), countdown(5), countdown(20)]
while tasks:  # means while tasks isn't empty
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:  # raised when we run out of values of the generator
        print("Task finished")
#using (next) is cheaper than using threads

###this example is valid for small fast operations. If there are big ones - they can be offloaded to a separate
# thread/process via threadsPoolExecutor or ProcessPoolExecutor

