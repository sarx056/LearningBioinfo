"""Week 1 - basic syntax, values, variables, conditionals and logic staments, functions, random and math modules"""

#function to find feet in miles

def miles_to_feet(feet):
    return 'feet in miles is ' + str(feet*5280 )
result = miles_to_feet(23)
print(result)

#making a function to know how many seconds are there in an hour, minute and a second

def total_seconds(hours, minutes, seconds):
    print('total number of seconds in an hour, a minute and a second are ')
    print(str(hours))
    print(str(minutes))
    print(str(seconds))
result2  = total_seconds(3600,60,1)
print(result2)

#challenge function, finding out triangle's area using herons formulae

import math
def point_distance(x0,y0,x1,y1):
    return ((x0-x1)**2 + (y0-y1)**2) ** 0.5

#using helper functions to compute the formula
def triangle_area(x0,y0,x1,y1,x2,y2):
    a = point_distance(x0,y0,x1,y1)
    b = point_distance(x0,y0,x2,y2)
    c = point_distance(x1,y1,x2,y2)
    s = (a + b + c) / 2
    return s*(s-a)*(s-b)*(s-c)** 0.5

#the function is now complete
def test(x0,y0,x1,y1,x2,y2):
    print('triangle with vertices ')
    print(str(x0) + str(y0) + (' and ')+ str(x1) + str(y1) + (' and ')+ str(x2) + str(y2))
    print('has an area of ' + str(triangle_area(x0,y0,x1,y1,x2,y2)))
    
#using test function to calculate the values
test(0,0,3,4,1,1)


#now lets make a lottery powerball
import random
def powerball():
    print('todays numbers are; ')
    print(random.randint(1,60))
    print(random.randint(1,60))
    print(random.randint(1,60))
    print(random.randint(1,60))
    print('and todays lottery number is! ')
    print(random.randint(1,60))
powerball()
powerball()
powerball()
#today we practicing conditionals and logic statements in python
#and also a mini project which i have no idea but lets try

#pig latin game
def pig_latin(word):
    """we're gonna add ay to words that start with consonants and way to the words
       starting with vowels """

    first_letter = word[0]
    rest_ofthe_word = word[1: ]

    if first_letter == 'a' or first_letter == 'e' or first_letter == 'o' or first_letter == 'u':
        return word + 'way!'
    else:
        return word + 'ay!'

test0 = pig_latin('ara')
test2 = pig_latin('pig')
test3 = pig_latin('hurray')
print(test0)
print(test2)
print(test3)































