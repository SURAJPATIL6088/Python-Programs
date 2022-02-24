# it is unorderd collection of elements 
# order is not maintained in the sets
# it does not accept the duplicate elements
# one element display at once time only

# two types
    # set data_type
    # frozen data_type

# in set we use the curly braces {}

set = {10, 20, 30, 40, 10, 30, 50}
print(set)

# update/ replace element
set.update([11,22,33])
print("After Updating the set : ",set)

# remove elements
set.remove(50)
print("After removing element 50 : ", set)