# f)Write a program to add an element, find union, intersection, difference, and clear the given sets.

set = {10, 20, 10, 40, 10}
set1 = {17, 28, 10, 40, 16}

set.update({11,22})

print("Union of Set : ",set.union(set1))

print("Intersection of Set : ",set.intersection(set1))

print("Difference of Set : ",set.difference(set1))

print(set.clear())
