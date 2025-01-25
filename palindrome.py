attempts=int(input())
while(attempts>0):
    attempts-=1
    sample=(input("enter the sample"))
    ans=list(sample)
    size=len(ans)
    if ans[0]==ans[size-1]:
        print("yes")
    else:
        print("no")