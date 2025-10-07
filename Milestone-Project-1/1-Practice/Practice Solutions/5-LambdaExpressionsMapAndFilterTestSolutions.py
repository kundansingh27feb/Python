"""
_____________________________________________________________________________________________

 Lambda Expressions, Map, and Filter
_____________________________________________________________________________________________

General Question: What Is lambda And where we can Use it?

General Answer:
_____________________________________________________________________________________________

Question1: Write a lambda function to add 10 to a number.
Answer1:
"""
add_10 = lambda x: x+10
print("Answer1: ", add_10(500))

#___________________________________________________________________________
#Question2: Write a lambda function to multiply two numbers.

#Answer2:

multiple = lambda a,b: a*b
print("\nAnswer2:", multiple(10,20))

#___________________________________________________________________________
# Question3: Sort a list of tuples by the second value using lambda.
# pairs = [(1, 3), (2, 2), (5, 1)]
#Output should be  [(5, 1), (2, 2), (1, 3)]

# Answer3:
PAIRS = [(1, 3), (2, 2), (5, 1)]
sorted_pairs = sorted(PAIRS, key=lambda x: x[1])
print("\nAnswer3: Sorted Pairs: ", sorted_pairs)


#___________________________________________________________________________
# Question4:  Use map() to square all numbers in a list.

# Answer4:
NUMS = [1,2,3,4]
squares = list(map(lambda x: x**2, NUMS))
print("\n Answer4: ", squares)


#___________________________________________________________________________
# #Question5: Convert a list of strings to uppercase. words = ["hello", "python", "lambda"]

#Answer5:

words = ["hello", "python", "lambda"]
uppercase = list(map(lambda x: x.upper(), words))
print("\nAnswer5: ", uppercase)

#___________________________________________________________________________
#Question6: Add two lists element-wise using map(). a = [1, 2, 3], b = [4, 5, 6] output should be
# [5, 7, 9]

#Answer6:

a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x,y: x+y, a,b))
print("\nAnswer6: ", result)
#___________________________________________________________________________
#Question7: Filter even numbers from a list. nums = [1, 2, 3, 4, 5, 6]

#Answer7:

NUMS = [1, 2, 3, 4, 5, 6]
evens=list(filter(lambda x: x%2==0,NUMS))
print("\nAnswer7: ", evens)

#___________________________________________________________________________
#Question8: Filter names starting with "A". names = ["Alice", "Bob", "Amanda", "Charlie"]
#Using 2 Methods

#Answer8:
#Method1:
names = ["Alice", "Bob", "Amanda", "Charlie", "amit"]
a_name = list(filter(lambda x: x.startswith("A") or x.startswith("a"),names))
print("\nAnswer7: ", a_name)

#Method2:
names = ["Alice", "Bob", "Amanda", "Charlie", "amit"]
a_name = list(filter(lambda x: x[0]=='A' or x[0]=='a',names))
print("\nAnswer8: ", a_name)

#___________________________________________________________________________
#Question9: Filter numbers greater than 50. numbers = [10, 55, 32, 100, 75]

#Answer9:

numbers = [10, 55, 32, 100, 75]
greate_50 = list(filter(lambda x: x>50,numbers))
print("\nAnswer9: ", greate_50)

#___________________________________________________________________________
#Question10: Use map() and filter() to get squares of even numbers only. nums = [1, 2, 3, 4, 5, 6]

#Answer10:
NUMS = [1, 2, 3, 4, 5, 6]
sq_of_even=list(map(lambda x: x**2,filter(lambda x: x%2==0,NUMS)))
print("\nAnswer10: Square Of Even Numbers: ",sq_of_even)

#___________________________________________________________________________
#Question11: Extract palindromes from a list of words. words = ["madam", "python", "level", "world"]

#Answer11:

words = ["madam", "python", "level", "world"]
palindromes = list(filter(lambda x:x==x[::-1],words))
print("\nAnswer11: palindrome Numbers: ",palindromes)

#___________________________________________________________________________
#Question12: Sort a list of dictionaries by "age" using lambda.
#people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]

#Answer12:
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]
sorted_people = sorted(people,key=lambda x:x["age"])
print("\nAnswer12: People sorted with age: ",sorted_people)

#___________________________________________________________________________
#Question13: Use map() to get the length of each string. words = ["Python", "Lambda", "Filter", "Map"]

#Answer13:
words = ["Python", "Lambda", "Filter", "Map"]
len_string = list(map(lambda x:len(x),words))
print("\nAnswer13: Leanth Of Each String: ",len_string)
#___________________________________________________________________________
#Question14: Combine map() and filter() to get cube of odd numbers only. nums = [1, 2, 3, 4, 5, 6]

#Answer14:

NUMS = [1, 2, 3, 4, 5, 6]
cb_odd = list(map(lambda x: x**3,filter(lambda x: x%2!=0,NUMS)))
print("\nAnswer14: cube of odd numbers only: ",cb_odd)

#___________________________________________________________________________
#Question15: Given a list of transactions, filter out failed ones and return only the amounts
# squared.
# transactions = [
#     {"id": 1, "amount": 100, "status": "success"},
#     {"id": 2, "amount": 200, "status": "failed"},
#     {"id": 3, "amount": 300, "status": "success"},
# ]

#Answer15:

transactions = [
    {"id": 1, "amount": 100, "status": "success"},
    {"id": 2, "amount": 200, "status": "failed"},
    {"id": 3, "amount": 300, "status": "success"},
]
result = list(map(lambda x: x["amount"]**2,filter(lambda x: x["status"]=="success",transactions)))
print("\n Answer15: ",result)

#___________________________________________________________________________

