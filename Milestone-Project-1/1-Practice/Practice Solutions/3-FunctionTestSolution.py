"""
___________________________________________________________________________

Function Assessment
___________________________________________________________________________

Function Practice Exercises
Problems are arranged in increasing difficulty:

Warmup - these can be solved using basic comparisons and methods
Level 1 - these may involve if/then conditional statements and simple methods
Level 2 - these may require iterating over sequences, usually with some kind of loop
Challenging - these will take some creativity to solve
___________________________________________________________________________
WARMUP SECTION:
----------------
Question1: LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5

Answer1:
"""

def less_of_2_even(a,b):
    """
    Function
    """
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print("Answer1:", less_of_2_even(4,8))

#___________________________________________________________________________
#Question2: ANIMAL CRACKERS: Write a function takes a two-word string and returns True
# if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
#Also use the upper or lower case function to match

#Answer2:
def animal_crackers(str1):
    """
    Function
    """
    wordlist = str1.split()
    return wordlist[0][0].upper() == wordlist[1][0].upper()
print("Answer2:", animal_crackers('Kundan kanha'))

#___________________________________________________________________________
#Question3: MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

#Answer3:
# def makes_twenty(n1,n2):
#     return (n1+n2)==20 or n1==20 or n2==20

def makes_twenty(p1,p2):
    """
    Function
    """
    return (p1+p2)==20 or p1==20 or p2==20
print("Answer3:", makes_twenty(2,3))

#___________________________________________________________________________
# LEVEL 1 PROBLEMS:
#----------------
#Question4: OLD MACDONALD: Write a function that capitalizes the first and
# fourth letters of a name
#old_macdonald('macdonald') --> MacDonald

#Answer4:

def old_macdonald(str1):
    """
    Function
    """
    if len(str1) > 3:
        return str1[:3].capitalize() + str1[3:].capitalize()
    else:
        return False
print("Answer4:", old_macdonald('MACDonalD'))


#___________________________________________________________________________
#Question5: MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

#Answer5:

def master_yoda(str1):
    """
    Function
    """
    return ' '.join(str1.split()[::-1])
print("Answer5:", master_yoda("My Name Is Kundan Singh! . . ."))



#___________________________________________________________________________
#Question6: ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
#NOTE: abs(num) returns the absolute value of a number

#Answer6:

def almost_there(num):
    """
    Function
    """
    return ((abs(100 - num) <= 10) or abs((200 - num) <=10))
print("Answer6:", almost_there(90))
#___________________________________________________________________________
#LEVEL 2 PROBLEMS:
#-----------------
#Question7: [Using 2 Method] FIND 33: Given a list of ints, return True if the array
# contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

#Answer7:
#Method1:
def has_33(nums):
    """
    Function
    """
    for i in range(0, len(nums)-1):
        # nicer looking alternative in commented code
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        else:
            return False
print("Answer7-1:", has_33([3, 3, 6]))

#Method1:
def has_33_2(nums):
    """
    Function
    """
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False
print("Answer7-2:", has_33_2([3, 3, 6]))

#___________________________________________________________________________
#Question8: PAPER DOLL: Given a string, return a string where for every character in the
# original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

#Answer8:

def paper_doll(str1):
    """
    Function
    """
    result = ''
    for char in str1:
        result += char * 3
    return result
print("Answer8:", paper_doll('Kundan'))
#___________________________________________________________________________
#Question9: BLACKJACK: Given three integers between 1 and 11, if their sum is less than or
# equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

#Answer9:

def blackjack(a,b,c):
    """
    Function
    """
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
print("Answer9:", blackjack(11,11,10))

#___________________________________________________________________________
#Question10: SUMMER OF '69: Return the sum of the numbers in the array, except ignore
# sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed
# by at least one 9). Return 0 for no numbers.
#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14

#Answer10:

def summer_69(arrs):
    """
    Function
    """
    total = 0
    add = True
    for num in arrs:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
print("Answer10:", summer_69([2, 1, 6, 9, 11]))

#___________________________________________________________________________
#CHALLENGING PROBLEMS:
#-------------------------
#Question11: SPY GAME: Write a function that takes in a list of integers and returns True if it
# contains 007 in order
 #spy_game([1,2,4,0,0,7,5]) --> True
 #spy_game([1,0,2,4,0,5,7]) --> True
 #spy_game([1,7,2,0,4,5,0]) --> False

#Answer11:
def spy_game(nums):
    """
    Function
    """
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
    return len(code) == 1
print("Answer11:", spy_game([1,2,4,1,0,7,5]))

#___________________________________________________________________________
#Question12: COUNT PRIMES: Write a function that returns the number of prime numbers that exist
# up to and including a given number
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

#Answer12:

def primes(num):
    """
    Function
    """
    prime_num = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            prime_num.append(x)
            x += 2
    print(prime_num)
    return len(prime_num)
print ("Answer12:", primes(1000))

#___________________________________________________________________________
#Question13: PRINT BIG: Write a function that takes in a single letter, and returns a 5x5
# representation of that letter
#print_big('a')

#out:   *
#      * *
#     *****
#     *   *
#     *   *
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to
# specific
# 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".

#Answer13:

#___________________________________________________________________________
