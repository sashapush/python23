def add_all (a1,a2,a3,a4):
    return a1+a2+a3+a4

vals = (1,2,6,5)
vals2={'a1':1,'a2':3,"a3":4,"a4":1}
print(add_all(2,3,4,5))
print(add_all(*vals))
print(add_all(**vals2)) #passing values as named arguments

#*args
#**kwargs
def add_all_new (*args):
    print(args) #returns tuple
    return sum(args)

print(add_all_new(5,7,3,2,4))

def add_all_pretty (**kwargs):
    for k,v in kwargs.items(): #kwargs is dictionary {"key":value}
        print(f"For {k} we have {v}") #returns tuple

add_all_pretty(username="assistant", length_of_iq = "6 inches")
#add_all_pretty({"username":"aaaa", "access_level":"admin"}) ##doesn't now it's keywords arguments - hence the **
add_all_pretty(**{"username":"aaaa", "access_level":"admin"})