def func1():
    print("Func1")

def func2(a):
    print("Func2",a)

def func3(a=10):
    print("Func3",a)


func1()
func2(2)
func3(3)
func3()