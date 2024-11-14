# Prompt the user to enter a number and store it in variable n as a string
n = input('Enter a number: ')

# Convert the input to an integer, as factorials are calculated on integers
n = int(n)

# Define a function called factorial that calculates the factorial of a given number n
def factorial(n):
    # Base case: If n is 1, return 1, as factorial(1) is defined to be 1
    if n == 1:
        return 1
    else:
        # Recursive case: Multiply n by the result of calling factorial with (n-1)
        # This breaks down the problem into smaller pieces until it reaches the base case
        return n * factorial(n - 1)

# Explanation of recursion:
# - Recursion is a technique where a function calls itself in order to solve a problem.
# - Here, the factorial function keeps calling itself with decremented values of n (n-1)
#   until it reaches the base case where n is 1.
# - At that point, the function stops calling itself, and the stack of function calls
#   begins to "unwind", multiplying each return value by n at each level of recursion.
#
# Example for factorial(4):
# 4 * factorial(3) --> 4 * (3 * factorial(2)) --> 4 * (3 * (2 * factorial(1))) --> 4 * 3 * 2 * 1 = 24
