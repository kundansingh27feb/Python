"""
___________________________________________________________________________

Numbers
___________________________________________________________________________

Question1: Write an equation that uses multiplication, division, an exponent, addition, and
subtraction that is equal to 100.25.
Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
"""

A = (60 + (10 ** 2) / 4 * 7) - 134.75
print(A)


# Question2: Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5)
# What is the value of the expression 4 * 6 + 5
# What is the value of the expression 4 + 6 * 5


EX1 = 4 * (6 + 5)
EX2 = 4 * 6 + 5
EX3 = 4 + 6 * 5
print(EX1, " ", EX2," ", EX3)

#
# Question3: What would you use to find a number’s square root, as well as its square?

# Square root:
#

SQROOT = 100 ** 0.5
SQUARE = 10 ** 2

print("Square root of 100 is: ",SQROOT," And sqaure of 10 is: ", SQUARE)


# ___________________________________________________________________________

# String
# ___________________________________________________________________________

# Question4: Given the string 'hello' give an index command that returns 'e'. Enter your code in
# the cell below:
#

STR1 = "hello"
print(STR1[1])

# Question5: Reverse the string 'hello' using slicing:

print(STR1[::-1])

# Question6: Given the string 'hello', give two methods of producing the letter 'o' using indexing.


print(STR1[4])
print(STR1[-1])


# ___________________________________________________________________________

# List
# ___________________________________________________________________________

# Question7: Build this list [0,0,0] two separate ways.
#

L1 = [0,0,0]
print(l1)
L2 = [0]*3
print(L2)

#
# Question8: Reassign 'hello' in this nested list to say 'goodbye' instead
# list3 = [1,2,[3,4,'hello']]

LIST3 = [1,2,[3,4,'hello']]
LIST3[2][2] = "goodbye"
print(LIST3)

# Question9: Sort the list below: list4 = [5,3,4,6,1]

LIST4 = [5,3,4,6,1]


# using builtin function. this will not sort the existing list if we need we can store the output to
# any other variable
# print(sorted(list4))

# using . This will sort the existing list


LIST4.sort()
print(LIST4)

# ___________________________________________________________________________

# Dictionaries
# ___________________________________________________________________________

# Question10: Using keys and indexing, grab the 'hello' from the following dictionaries:
# d = {'simple_key':'hello'} And d = {'k1':{'k2':'hello'}}

D = {'simple_key':'hello'}
print(D['simple_key'])

D = {'k1':{'k2':'hello'}}
print(D['k1']['k2'])

D = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(D['k1'][0]['nest_key'][1][0])

D = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(D['k1'][2]['k2'][1]['tough'][2][0])

# Question11:  Can you sort a dictionary? Why or why not?
# **Answer: No! Because normal dictionaries are mappings not a sequence. **

# ___________________________________________________________________________

# Tuples
# ___________________________________________________________________________

# Question12: What is the major difference between tuples and lists?

# **Answer: Tuples are immutable!

# Question13: How do you create a tuple?


T = (1,4,6,9)

# ___________________________________________________________________________

# Sets
# ___________________________________________________________________________

# Question14: What is unique about a set?

# **Answer: They don't allow for duplicate items!

# Question15: Use a set to find the unique values of the list below:
# list5 = [1,2,2,33,4,4,11,22,3,3,2]

LIST5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(LIST5))


# ___________________________________________________________________________

# Booleans
# ___________________________________________________________________________

# Question16: What will be the resulting Boolean of the following pieces of code (answer fist then
# check by typing it in!) a = 2 > 3, a = 3 <= 2, a = 3 == 2.0, a = 3.0 == 3, a = 4**0.5 != 2

VOL1 = 6
VOL2 = 10
VOL3 = 0.5
A = VOL1 > VOL2
print(A)
A = VOL1 <= VOL2
print(A)
A = VOL1 == VOL2
print(A)
A = VOL1 == VOL2
print(A)
A = VOL1**VOL3 != VOL2
print(A)


# Final Question17: What is the boolean output of the cell block below?
# l_one = [1,2,[3,4]]
# l_two = [1,2,{'k1':4}]
# l_one[2][0] >= l_two[2]['k1']
#

L_ONE = [1,2,[3,4]]
L_TWO = [1,2,{'k1':4}]
FINAL = L_ONE[2][0] >= L_TWO[2]['k1']
print(FINAL)
