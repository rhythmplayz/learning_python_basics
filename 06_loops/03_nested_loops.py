for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()


print()
cnt = 10
while cnt > 0:
    for j in range(cnt):
        print(j, end=" ")
    print()
    cnt -= 1

print()
cnt = 10
for j in range(cnt):
    while j>0:
        print(j, end=" ")
        j-=1
    print()
