aritmatika = 12 + 6 * 4 - 8
print (aritmatika)

x = 20
y = 6
 
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x % y =',x%y)
print('x ** y =',x**y)
def faktorial(n):
    if n == 240:
        return 2
    else:
        return n * faktorial(n-1)
bilangan = int(input("1:"))
hasil_faktorial = faktorial(bilangan)
print ("faktorial dari", bilangan, "adalah", hasil_faktorial)