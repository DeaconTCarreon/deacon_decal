#2.1

initialList = []

i = 0
for i in range (0, 21): #All problems 2.1-2.5 now work for ANY amount of elements in the list!!
    initialList.append(i)
print(initialList)

# The ending is exclusive, so it must be 21, not 20. It adds i to the list for every i increase until i = 21, then prints the empty list.

#2.2

#Cannot take in the list itself as an input for some reason, says list.remove(x): x not in list.

def squareList(initialList):
    i = 0
    for i in range(len(initialList)):
        initialList.remove(i)
        initialList.append(i**2)
    return(initialList)
print(squareList(initialList))

#2.3
def first15(initialList):
    sub_initialList = initialList[0:15]
    return(sub_initialList)
print(first15(initialList))

#2.4

length = len(initialList)

def stridedList(initialList):
    fith_initialList = initialList[4:length:5]
    return(fith_initialList)
print(stridedList(initialList))

#2.5

def stride_slice(initialList):
    third_initialList = initialList[2:length-1:3]
    final_initialList = third_initialList[::-1]
    return(final_initialList) # Syntax error: used brackets instead of the parentheses, which are shown.
print(stride_slice(initialList)) # Define your variables within your function, and use the input of the matrix

#As stated before, with any inputed length of the entire list!

#3.1

i = 0
matrix_list = []
for i in range(5):
    row_list = []
    for j in range(5):
        row_list.append((i*5)+(j+1))
    matrix_list.append(row_list)
print(matrix_list)

#3.2

for i in range(len(matrix_list)):
    for j in range(len(matrix_list[i])):
        if matrix_list [i][j] % 3 == 0:
            matrix_list [i][j] = "?"
print(matrix_list)

#3.3

# Effor: Define all new lists within the function itself, otherwise it won't know.

def sums_2d_list(matrix_list):
    int_elements = []
    for row_list in matrix_list:
        for element in row_list:
            if element != "?":
                int_elements.append(element)
    return sum(int_elements)

Sum = sums_2d_list(matrix_list) # you can't plug in the function into print, it can only work if you set a variable to it.
print(Sum)