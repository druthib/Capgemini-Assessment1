n=int(input("enter n:"))
i=0
j=0
while(i<n+1):
    while(j<i):
        print("*"*i)
        j+=1
    i+=1    
print('reverse of the pattern')
i=0
j=n
while(i>=0 and i<n):
    while(j<=n and j>0):
        print("*"*j)
        j-=1
    i+=1
 
# n=int(input())
# i=0
# while(i<n+1):
#     j=n
#     while(j>=i):
#         print("*"*j)
#         j-=1
#     i+=1 
    