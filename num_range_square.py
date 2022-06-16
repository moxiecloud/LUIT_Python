# enter an integer
# check if integer is between 1 and 20, inclusive
# loop through the range of numbers 
# find square root of each number and print

n = int(input())
if (n >=1 and n <= 20):
    n = range(0, n)
    for x in n:
        y = x**2
        print(y)
else:
    print("You must enter a number greater than equal to 1 or a number less than or equal to 20")
