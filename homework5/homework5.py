# # 1.1

# pwd

# # 1.2

# ls

# 1.3

# git pull brianna_repo/python_decal

# 1.4

# mv homework.py ~/python_decal/judy_decal/homework/

# 1.5

# cat homework.py

# 1.6

# vim homework.py

# 1.7

# git add .
# git commit -m "Insert Text"
# git push

# 1.8

# Calling "git add ." will help fix this. The error arises if you only save your homework on just vs code, and the computer 
# thinks there are two, so it's important to do "git add ." constantly after making major changes.

# 1.9

# cd ~/Recents/

# 2.1

data = 3.14

def checkDataType(data):
    value = type(data)
    return(value)

DataType = checkDataType(data)
print(DataType)


# 2.2

input = 7

def evenOrOdd(input):
    if (input%2 == 0):
        value = "Even"
    else: # Error: Forgot colon
        value = "Odd"
    return value

evenOdd = evenOrOdd(input)
print(evenOdd)

# 3

numbers = [1, 2, 3, 4, 5]

def sumLists(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return(sum)

sumLoop = sumLists(numbers)
print(sumLoop)


# 4.1

list = ['a', 'b', 'c']

def duplicateList(list): # Takes 0 propositional arguments but 1 was given, so put in list in the parentheses.
    newlist = []
    for i in range(0, len(list)):
        newlist.append(list[i])
        newlist.append(list[i])
    return(newlist)

duplicated = duplicateList(list) # Set it as a value first
print(duplicated)

# 4.2

def square(num): # Forgot to add the colon to the end of this line to indicate it as a function
    return num * num