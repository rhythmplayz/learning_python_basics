# basic
a, b = 10, 20
mn = a if a < b else b
print(a,b,mn)

# nested
n = -5
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)

# using tuple
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)

# using dictionary
a = 10
b = 20
m1 = {True: a, False: b}[a > b]
print(m1)

# using lambda
a = 10
b = 20
m1 = (lambda x, y: x if x > y else y)(a, b)
print(m1)