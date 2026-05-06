def evenOdd(x):
    if x & 1 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(2))
print(evenOdd(3))
print()

def func1(a = 10):
    print(a)

func1()
func1(1)
print()

def func2(a,b):
    print(a,b)

func2(1,2)
func2(b=1,a=2)
print()

def func3(a,b,/,c,d,*,e):
    print(a,b,c,d,e)

func3(1,2,d=3,c=4,e=5)
print()

def func4(*args,**kwargs):
    print(args)
    print(kwargs)

func4(1,2,d=3,c=4,e=5)
print()
