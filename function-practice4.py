# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(*num):
    return max(num)


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*num):
    total = 1
    for i in num:
        total *= i 
    return total


# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]



# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(num, start_num, end_num):
    
    if num >= start_num and num <= end_num:
        return True
    else: 
        return False
    

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):

    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')
    
        # first element is always 1
        C = 1
        for j in range(1, i+1):
    
            # first value in a line is always 1
            print(' ', C, sep='', end='')
    
            # using Binomial Coefficient
            C = C * (i - j) // j
        print()



print(num_within(1,1,5))
print(num_within(2,1,5))
print(num_within(3,1,5))
print(num_within(4,1,5))
print(num_within(5,1,5))
print(num_within(0,1,5))
print(num_within(6,1,5))

print(max_num(3, 10, 1))

print(mult_list(2,2,2,4,2))

print(rev_string("bat"))

n = 3
pascal(n)