import math
print('\t___CALCULATOR___')
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a > b:
        a-=b
        return  a
    else:
        b-=a
        return b
def mul(a,b):
        a*=b
        return a
def div(a,b):
    q=a/b
    r=a%b
    print('\nThe quotient is: %s' %q)
    print('\nThe remainder is: %s'%r)
def sqr(a):
        x=math.sqrt(a)
        return x
while (True):
        print('\nChoose the operation you want to perform:')
        print('\n\t1.ADDITION')
        print('\n\t2.SUBTRACTION')
        print('\n\t3.MULLTIPLICATION')
        print('\n\t4.DIVISION')
        print('\n\t5.SQUARE ROOT')
        print('\n\t6.EXIT')
        choice = int(input('>'))
        if choice==1:
            print('\n\nEnter the two nos.:')
            num1=int(input('>'))
            num2 = int(input('>'))
            s=sum(num1,num2)
            print('The sum is: %s' %s)
        elif choice==2:
            print('\n\nEnter the two nos.:')
            num1 = int(input('>'))
            num2 = int(input('>'))
            m = sub(num1, num2)
            print('The difference is: %s' %m)
        elif choice == 3:
            print('\n\nEnter the two nos.:')
            num1 = int(input('>'))
            num2 = int(input('>'))
            p = mul(num1, num2)
            print('The product is: %s' %p)
        elif choice == 4:
            print('\n\nEnter the two nos.:')
            num1 = int(input('>'))
            num2 = int(input('>'))
            div(num1, num2)
        elif choice == 5:
            print('\n\nEnter the two nos.:')
            num1 = int(input('>'))
            r=sqr(num1)
            print('The square root is: %s' %r)
        else:
            print('\nYou chose to exit.Bye......')
            break
