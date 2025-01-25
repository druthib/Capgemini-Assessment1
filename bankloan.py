salary=float(input("enter your salary"))
age=int(input('enter your age'))
creditScore=int(input('enter your credit score'))
def loanApproval(salary,age,creditScore):
    if salary<30000:
        print('The salary is too low to grant loan. Sorry.')
    elif age<18 or age>65:
        print('Loans will not be sanctioned to people under this age group. Sorry.')
    elif creditScore<700:
        print('The credit score is too low to grant loan. Sorry.')
    else:
        print('Congrats. You are eligible for the loan')    
loanApproval(salary,age,creditScore)