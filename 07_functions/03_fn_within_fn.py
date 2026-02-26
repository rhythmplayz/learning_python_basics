def f1(a):
    print(a)
    def f2(a):
        if a%2==0:
            print("Even")
        else:
            print("Odd")
    f2(a)

f1(2)
f1(3)