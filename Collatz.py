print('This is a Collatz conjecture calculator')
while True:
    a = x = int(input('Type in an integer: '))
    i=0
    while x != 1:
        mod = x % 2
        if (mod == 0):
            x = x / 2
            i = i + 1
        else:
            x = x * 3 + 1
            i = i + 1
        print(x)
    print (str(a) + ' reaches 1 after ' + str(i) + ' iterations')
    print (' ')
