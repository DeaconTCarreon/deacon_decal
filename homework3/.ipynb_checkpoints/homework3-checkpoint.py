#1

#Want x**Y but cannot use it.
x = 4
y = 2

def computePower(x,y):

    i = 1
    result = 0
    while i < y:
        result += x * x
        i += 1
    print(result)
    
computePower(x,y)

#2

temperatures = [44, 57, 68, 52, 39, 55, 63]

def findTemps(x, y):
    
    y = max(temperatures)
    x = min(temperatures)
    hi_low = (x, y)
    return(hi_low)

print(findTemps(x, y))

#3

day = 7 # 1 is Monday, 6 is Saturday, 

def isWeekend(day):
    x=day
    if x==6:
        print("True")
    elif x==7:
        print("True")
    else:
        print("False")

isWeekend(day)

#4

distance = 100 # miles
fuel = 32 # gallons

def fuel_efficiency(distance, fuel):
    x = distance
    y = fuel
    mpg = x/y
    return(mpg)

print(fuel_efficiency(distance, fuel))

#5

n = 12345

def decodeNumbers(n):
    
    last_digit = n % 10 # Takes out the last digit with the modulo
    n_next = n - last_digit # Takes out the last digit
    n_reduced = n_next / 10 # Takes out the zero at the end, lowers order of magnitude. But it is now a float
    n_integer = int(n_reduced) # Converts the previous number from a float to an integer.
    n_large = last_digit * (10000) # Converts our last digit last_digit into a larger value to be added.
    n_final = n_large + n_integer # Adds up the now final digit with the shrunken number

    print(n_final)

decodeNumbers(n)
#Works for any five digit integer!

#6.1

nums = [3552, 345, 24, 120, 512]
 
def find_max(nums):
    for i in range <= nums:
        print(i)
    return

find_max(nums)

def find_min(nums):
    for i in range

#6.2

def find_min_max(nums):
    while nums < 10:
        print(i)

#7

text = "This is a line of test text"

#8

num = 9999

def digital_root(num):

    digit_Four = int(num / 1000) # Isolates the fourth digit as its own number, and then turns it into an integer
    digit_Three = int((num - (digit_Four * 1000)) / 100) # Isolates the third digit as its own number, turns it into an integer
    digit_Two = int((num - ((digit_Four * 1000) + (digit_Three * 100))) / 10) # Isolates the second digit as it's own number, turns it into an integer
    digit_One = int(num - ((digit_Four * 1000) + (digit_Three * 100) + (digit_Two * 10)))
    root = digit_Four + digit_Three + digit_Two + digit_One
    print(root)

digital_root(num)
# Works for ANY four digit integer!