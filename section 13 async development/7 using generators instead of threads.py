#it's as if threading, but less efficient lul
def countdown(n):
    while n > 0:
        yield n #at this point command is suspended
        n -= 1


c1 = countdown(10)
c2 = countdown(20)
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))
#2 tasks yielding control of the main thread to one another
#print(next(c))  # 10
#print(next(c))  # 9
#print(next(c))  # 8
