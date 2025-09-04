# input() takes in a line of input
# int() converts a string to an integer
for _ in range(int(input()):
    # this is a combo of list comprehension and int to parse a list of numbers
    # note that it doesn't specify a list length
    # ex: 1 2 3 4 5
    a = [int(x) for x in input().split()]

    # this takes in specifically 2 numbers, and assigns the values to the variables left and right
    left, right = map(int, input().split())
    
