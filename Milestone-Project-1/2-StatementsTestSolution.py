#___________________________________________________________________________
# Statements Assessment
#___________________________________________________________________________

#Question1: Use for, .split(), and if to create a Statement that will print out words that start
# with 's'. Also what split function do?: st = 'Print only the words that start with s in this
# sentence'

st = 'Print only the words that start with s in this sentence Sanju'
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)
#Split finction split the sentence in a list
print(st.split())

#___________________________________________________________________________

#Question2: Use range() to print all the even numbers from 0 to 10.
print(list(range(0,11,2)))

#___________________________________________________________________________

#Question3: Use List comprehension to create a list of all numbers between 1 and 50(using 2 method)
# that are divisible by 3.

#Method1:
num = [x for x in range(1,51) if x%3 == 0]
print(num)

#Method2:
num = []
for x in range(1,51):
    if x%3 == 0:
        num.append(x)
print(num)

#___________________________________________________________________________

#Question4: Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word," <-- Has an even length!!")

#
#Question5: Write a program that prints the integers from 1 to 100. But for multiples of three
# print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which
# are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)

#___________________________________________________________________________

#
#Question6: Use a List Comprehension to create a list of the first letters of every word in the
# string below: Use a List Comprehension to create a list of the first letters of every word in
# the string below(Use 2 mothod to solve this): st = 'Create a list of the first letters of every
# word in this string'

#Method 1:
st = 'Create a list of the first letters of every word in this string'
list1=[]
for word in st.split():
    list1.append(word[0])
print(list1)

#Method 2:

list1 = [word[0] for word in st.split()]
print(list1)
#___________________________________________________________________________