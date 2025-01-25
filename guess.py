import random
randomNumber=random.randint(1,100)
print(randomNumber)
def guess(randomNumber):
    numberOfAttempts=int(input())
    while(numberOfAttempts>0):
        numberOfAttempts-=1
        user_guess=int(input("enter your guess"))
        if(user_guess==randomNumber):
            print("Congrats.You guessed it right!!")
        elif(user_guess>randomNumber):
            print('Too High')
            print("Try again")
        else:
            print('Too Low')
            print("Try again")
guess(randomNumber)

    