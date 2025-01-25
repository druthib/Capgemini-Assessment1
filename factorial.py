def factorial(num):
    ans=1
    for i in range(1,num+1):
        ans *=i
    return ans
number=int(input("enter the number"))
if number<0:
    print("Factorial is not defined for negative numbers")
    print("please enter a non negative integer.")
else:
    fact=factorial(number)
    print(f"the factorial of {number}:{fact}")
