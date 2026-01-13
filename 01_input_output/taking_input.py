name = input("What is your name?")
print("Your name is:",name)
num = input("What is your favourite number?")

print("\nPython takes input as strings")
print("Type of name variable:", type(name), name)
print("Type of num variable:", type(num), num)
print()

# Converting the type of input

i = int(input("Enter a integer:"))
print(type(i))
print()

f = float(input("Enter a floating number:"))
print(type(f))
print()

# taking multiple inputs

x,y = input("Enter two numbers:").split(" ")
print("First number is:",x)
print("Second number is:",y)
print()