# range data-type it gives the sequence of numbers
#
# syntax
# variable-name = range(10)

vn = range(10)
print(vn)       # o/p : range(0, 10)

# start from 1 and end with 10-1
for i in range(1,10):   # it stop at 9
    print(i)    # o/p : 0 1 2 3 4 5 6 7 8 9 

# step function
# start from 1 and end with 10-1 and step to 2
for i in range(2, 10, 2):
    print(i)
