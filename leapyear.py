def isLeapYear(year):
    if year%4==0:
        if year%100==0:
            return year%400==0
        return True
    return False

t=int(input())
while(t>0):
    t-=1
    year=int(input("enter the year:"))
    if isLeapYear(year):
        print("It is Leap Year")
    else:
        print("Its not Leap Year")