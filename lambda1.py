from tkinter import N


remainder = lambda num: num % 2
print(remainder(5))

product = lambda x, y: x*y
print(product(2,3))

def testfunct(num):
    print(num)
    return lambda x: x*num

result10 = testfunct(10) # creates a function called result10, the argument is 10, but we don't know x yet 
# we are creating two variations of the same function
result100 = testfunct(100)

print(result10(9))
print(result100(9))
# num is 10 and x is 9

# anoth way to do this:
result10 = lambda x: x*10
result100 = lambda x: x*100

# filter
numbers_list = [2,6,8,10,11,4,7,13,17,0,3,21]
filtered_list = list(filter(lambda num: (num>7), numbers_list)) # all elements > 7 # gibberish without the list
print(filtered_list)

# map function
def addition(n):
    return n + n
numbers = [1,2,3,4]
result = map(addition, numbers)
print(list(result)) # prints gibbersh without the list

result = list(map(lambda num: num+num, numbers))
print(result)

numbers = (1,2,3,4)
numbers2 = (5,6,7,8)
result = list(map(lambda x,y: x+y, numbers, numbers2))
print(result)

# Example on Zip
list1 = ['a','b','c']
list2 = [1,2,3]
list3 = [1.5,3.1,5.7]

for item in zip(list1,list2,list3): 
# combining 3 different lists to produce one iterable so that you don't have to iterate 3 times
    l1,l2,l3 = item
    print(l1)
    print(l2)
    print(l3)