lst_num = []

n = int(input("Enter  size of List : "))

print("\n")

for i in range(0, n):
    print("Enter num at index", i, )
    num = int(input())
    lst_num.append(num)

print("User list is ", lst_num)

# empty lists
Even = []
Odd = []

for i in lst_num:
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print("List of even : ", Even)
print("List of odd : ", Odd)
