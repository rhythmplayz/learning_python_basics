# same value
a = b = c = d = e = f = g = 1
print(a,b,c,d,e,f,g)
print()

#different values
a,b,c = 1,2,3
print(a,b,c)
print()
a,b,c,*d = 1,2,3,4,5
print(a,b,c,d)
print()

a,b,*c,d,e = 1,2,3,4,5,6
print(a,b,c,d,e)
print()