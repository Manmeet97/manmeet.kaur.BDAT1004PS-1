"""Question 1
What data type is each of the following (evaluate where necessary)?
5  -> Int
5.0 -> Double
5 > 1 -> Boolean
'5' -> String
5 * 2 ->Int32
'5' * 2 -> string
'5' + '2' -> string
5 / 2 -> Int32
5 % 2 -> Double
{5, 2, 1} -> List
5 == 3 -> Boolean
Pi (the number) -> Double
"""

##############################################################################

"""Question 2
Write (and evaluate) python expressions that answer these questions:
"""

# a. How many letters are there in 'Supercalifragilisticexpialidocious'?

print(f"Number of letters in 'Supercalifragilisticexpialidocious' are {len('Supercalifragilisticexpialidocious')}")

# b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? 
string = "Supercalifragilisricexpialidocious" 
substring = "ice"
if substring in string:
    print("yes it contains")
else:
    print("no, it doesnt contains")
    
# c. Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn? 
list1=["Supercalifragilisticexpialidocious","Honorificabilitudinitatibus","Bababadalgharaghtakamminarronnkonn"]
print(max(list1, key=len))
 
# d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?
list2 = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
list2.sort()
print(f"The first one is {list2[0]}")
print(f"The lastt one is {list2[-1]}")


##############################################################################################

"""Question 3
Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
sides of a triangle and returns the area of the triangle. By Heron's formula, the area 
of a triangle with side lengths a, b, and c is
s(s - a)(s -b)(s -c)
, where 
s = (a+b+c)/2"""

a = float(input('Enter the length of 1st side= '))  
b = float(input('Enter the length of 2nd side '))  
c = float(input('Enter the length of 3rd side= '))  
s = (a + b + c) / 2  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('Area of the triangle is %0.3f' %area)


##############################################################################################
"""Question 4
Write a program in python to separate odd and even integers in separate arrays. Go 
to the editor
Test Data :
Input the number of elements to be stored in the array :5
Input 5 elements in the array :
element - 0 : 25
element - 1 : 47
element - 2 : 42
element - 3 : 56
element - 4 : 32
Expected Output:
The Even elements are:
42 56 32
The Odd elements are :
25 47
"""

A= [25,47,42,56,32]
evenlist =[]
oddlist=[]
for i in A:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even lists:" , " ".join(str(i) for i in evenlist))
print("odd lists: " , " ".join(str(i) for i in oddlist))


##############################################################################################
"""Question 5"""

"""a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False 
depending on whether the point (x,y) lies in the rectangle with lower left 
corner (x1,y1) and upper right corner (x2,y2).
 inside(1,1,0,0,2,3)
True
 inside(-1,-1,0,0,2,3)
False"""

def inside(x, y, x1, y1, x2,
              y2) :
    if (x > x1 and x < x2 and
        y > y1 and y < y2) :
        return True
    else :
        return False

print(inside(1,1,0,0,2,3))  
print(inside(-1,-1,0,0,2,3))


"""b. Use function inside() from part a. to write an expression that tests whether 
the point (1,1) lies in both of the following rectangles: one with lower left 
corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower 
left corner (0.5, 0.2) and upper right corner (1.1, 2)"""

print("Do (1,1) lies in inside both the rectangles ", inside(1, 1, 0.3, 0.5, 1.1, 0.7) and inside(1, 1, 0.5, 0.2, 1.1, 2))

##############################################################################################
"""Question 6
16. You can turn a word into pig-Latin using the following two rules (simplified):
• If the word starts with a consonant, move that letter to the end and append 
'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
• If the word starts with a vowel, simply append 'way' to the end of the word. 
For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For 
our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case 
characters. Your output should always be lower case however."""

def pig(word):
    word=word.lower()
    if word[0] in ['a','e','i','o','u']:
        return word+"way"
    else:
        return word[1:]+word[0]+"ay"
    
print(pig("enter"))
print(pig("happy"))
##############################################################################################

"""Question 7
File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. 
Write a function bldcount() that reads the file with name name and reports (i.e., 
prints) how many patients there are in each bloodtype"""

def bldcount(filename):
    #reading the file
    x = open(filename,'r')
    words = x.readline()
    l = []
    blood_types = ['A','B','AB','O','OO']
    # spliting the words and storing them into a list
    l.append(words.split(" ")) 
    # checking the count for each blood group
    for types in blood_types:
        print(f"There are {l[0].count(types)} patients of blood type {types}")
bldcount('bloodtype1.txt')
##############################################################################################
"""Question 8
Write a function curconv() that takes as input:
1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 
'EUR' for the Euro)
2. an amount
and then converts and returns the amount in US dollars."""

def curconv(currency, amount):
    # reading the file
    cur_file = open('currencies.txt')
    currencies = {}
    lines = cur_file.readlines() 
    # storing the currency in the key and it's corresponding $ value and name in value.
    for x in lines:
        currencies[x[:3].strip()] = x[4:].split("\t")
    value = currencies[currency][0].strip()
    return amount * float(value)
    
print(curconv('EUR', 100))
print(curconv('JPY', 100))

##############################################################################################
"""Question 9
Each of the following will cause an exception (an error). Identify what type of 
exception each will cause."""

# Trying to add incompatible variables, as in adding 6 + ‘a’
#-> Unsupported type

# Referring to the 12th item of a list that has only 10 items
#-> Out of index

# Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)
#-> domain error

# Using an undeclared variable, such as print(x) when x has not been defined 
#-> variable not defined

# Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.
#-> No such directory found

##############################################################################################
"""Question 10
Encryption is the process of hiding the meaning of a text by substituting letters in the 
message with other letters, according to some system. If the process is successful, no 
one but the intended recipient can understand the encrypted message. Cryptanalysis
refers to attempts to undo the encryption, even if some details of the encryption are 
unknown (for example, if an encrypted message has been intercepted). The first step 
of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. 
Assume that the string letters is already defined as 
'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies()
that takes a string as its only parameter, and returns a list of integers, showing the 
number of times each character appears in the text. Your function may ignore any 
characters that are not in letters"""

def frequencies(text):
    
    #set of alphabets
    alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    total_characters = []
    dict_alphabets = {}
    # appending the all the words
    for word in text:
        for alpha in word:
            if alpha.isalpha():
                total_characters.append(alpha)
    # checking the count of each alphabet
    for alpha in alphabets:
        if alpha in total_characters:
            dict_alphabets[alpha] = total_characters.count(alpha)
        else:
            dict_alphabets[alpha] = 0
            
    # printing the count of the alphabets present in the total_character list
    return list(dict_alphabets.values())

print(frequencies('The quick red fox got bored and went home.'))
print(frequencies('apple'))
##############################################################################################
