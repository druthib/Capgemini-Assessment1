listOfNumbers=list(map(int,input("enter the numbers").split()))
print(listOfNumbers)
highest=max(listOfNumbers)
secondHighest=0
for number in listOfNumbers:
    if(number<highest and number>secondHighest):
        secondHighest=number
print(secondHighest)


