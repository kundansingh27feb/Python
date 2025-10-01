"""
___________________________________________________________________________

Numbers
___________________________________________________________________________

Question1: Write an equation that uses multiplication, division, an exponent, addition, and
subtraction that is equal to 100.25.
Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
"""

a = ((60 + (10 ** 2) / 4 * 7) - 134.75)
print(a)

"""
Question2: Answer these 3 questions without typing code. Then type code to check your answer.
What is the value of the expression 4 * (6 + 5)
What is the value of the expression 4 * 6 + 5
What is the value of the expression 4 + 6 * 5
"""

ex1 = 4 * (6 + 5)
ex2 = 4 * 6 + 5
ex3 = 4 + 6 * 5
print(ex1, " ", ex2," ", ex3)

"""
Question3: What would you use to find a number’s square root, as well as its square?

Square root:
"""

sqroot = 100 ** 0.5
square = 10 ** 2

print("Square root of 100 is: ",sqroot," And sqaure of 10 is: ", square)

"""
___________________________________________________________________________

String
___________________________________________________________________________

Question4: Given the string 'hello' give an index command that returns 'e'. Enter your code in
the cell below:
"""

str1 = "hello"
print(str1[1])

# Question5: Reverse the string 'hello' using slicing:

print(str1[::-1])

# Question6: Given the string 'hello', give two methods of producing the letter 'o' using indexing.


print(str1[4])
print(str1[-1])

"""
___________________________________________________________________________

List
___________________________________________________________________________

Question7: Build this list [0,0,0] two separate ways.
"""

l1 = [0,0,0]
print(l1)
l2 = [0]*3
print(l2)

"""
Question8: Reassign 'hello' in this nested list to say 'goodbye' instead
list3 = [1,2,[3,4,'hello']]
"""

list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
print(list3)

# Question9: Sort the list below: list4 = [5,3,4,6,1]

list4 = [5,3,4,6,1]

"""
using builtin function. this will not sort the existing list if we need we can store the output to
any other variable
print(sorted(list4))

using . This will sort the existing list
"""

list4.sort()
print(list4)

"""
___________________________________________________________________________

Dictionaries
___________________________________________________________________________

Question10: Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'} And d = {'k1':{'k2':'hello'}}
"""

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

"""
Question11:  Can you sort a dictionary? Why or why not?
**Answer: No! Because normal dictionaries are mappings not a sequence. **

___________________________________________________________________________

Tuples
___________________________________________________________________________

Question12: What is the major difference between tuples and lists?

**Answer: Tuples are immutable!

Question13: How do you create a tuple?
"""

t = (1,4,6,9)

"""
___________________________________________________________________________

Sets
___________________________________________________________________________

Question14: What is unique about a set?

**Answer: They don't allow for duplicate items!

Question15: Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
"""

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

"""
___________________________________________________________________________

Booleans
___________________________________________________________________________

Question16: What will be the resulting Boolean of the following pieces of code (answer fist then
check by typing it in!) a = 2 > 3, a = 3 <= 2, a = 3 == 2.0, a = 3.0 == 3, a = 4**0.5 != 2
"""

a = 2 > 3
print(a)
a = 3 <= 2
print(a)
a = 3 == 2.0
print(a)
a = 3.0 == 3
print(a)
a = 4**0.5 != 2
print(a)

"""
Final Question17: What is the boolean output of the cell block below?
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
l_one[2][0] >= l_two[2]['k1']
"""

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
final = l_one[2][0] >= l_two[2]['k1']
print(final)
