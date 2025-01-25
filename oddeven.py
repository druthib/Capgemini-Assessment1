no=input("enter the numbers").split()
listOfNumbers=[int(i) for i in no]
print(listOfNumbers)
oddLists=[]
evenLists=[]
for i in listOfNumbers:
    if i%2==0:
        evenLists.append(i)
    else:
        oddLists.append(i)
print(evenLists)
print(oddLists)
