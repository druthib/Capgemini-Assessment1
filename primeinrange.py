num1=int(input('enter the first number'))
num2=int(input('enter the second number'))
def isPrime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def primeRange(num1,num2):
    print(f"Prime numbers from {num1} to {num2}:")
    for n in range(num1,num2+1):
        if isPrime(n):
            print(n,end=" ")
primeRange(num1,num2)


