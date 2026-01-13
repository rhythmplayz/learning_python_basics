# print() function prints value regardless of type and auto adds new line
print("a")
print(1)
print(2.0)
print(False)

lst = [1,2,3,4,5]
print(lst)
print()

# elements can be printed at once
print("a",1,2.0,False,lst)
print()

# default line-end is "\n" and separator is " ", these can be changed
print("a",1,2.0,False,lst, sep="; ",end=" New End\n")
print()