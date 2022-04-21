''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [2, 4, 6, 8, 10]
odds = [1, 3, 5, 7, 9]

even_list = list(filter(lambda num: num in evens, mylist)) 
print(even_list)

odd_list = list(filter(lambda num: num in odds, mylist)) 
print(odd_list)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
characters = list(filter(lambda day: len(day) ==6, weekdays )) 
print(characters)

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
up_colors = list(filter(lambda color: color not in ['orange', 'black'], colors)) 
print(up_colors)


''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

mylist = list(filter(lambda x: x not in list2, list1))
print(mylist)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
colors = ['red', 'black', 'white', 'green', 'orange']
sub_string = 'ack'
up_colors = list(filter(lambda x: sub_string in x, colors)) 
print(up_colors)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
string = '456TRp'

checks = [lambda string: any(x.isupper() for x in string), 
        lambda string: any(x.islower() for x in string),  
        lambda string: any(x.isdigit() for x in string),  
        lambda string: len(string) >= 8]

result = [x for x in [i(string) for i in checks] if x != True]
if not result:
    print("Password:{} is verified.".format(string))
else:
    print("Password:{} is not valid.".format(string))


''' 7)
Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_scores = sorted(original_scores, key = lambda x: x[1])
print(sorted_scores)

