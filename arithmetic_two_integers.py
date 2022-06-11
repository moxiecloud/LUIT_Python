if __name__ == '__main__':
    a = int(input('enter 1st: '))
    b = int(input('enter 2nd: '))

if not (1<=a<=10**10) or not (1<=b<=10**10):
    print("You entered an invalid number")
else:
    print(a+b)
    print(a-b)
    print(a * b)
