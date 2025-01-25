password=input('enter your password to check')
def passwordStrengthChecker(password):
    specialchar="!@#$%^&*()_+-=;'/.,<>?:{|"
    digit="01234156789"
    upper_avail=False
    lower_avail=False
    digit_avail=False
    special_avail=False
    
    if len(password)<8:
        print("The password is weak. It must contain at least 8 Characters")
    else:
        print("The password is strong")
    for char in password:
        if char.isupper():
            upper_avail=True
        if char.islower():
            lower_avail=True
        if char in digit:
            digit_avail=True
        if char in specialchar:
            special_avail=True
    if upper_avail:
        print("The password is strong.It contains one or more uppercase letters")
    else:
            print("The password is weak.It must have at least one uppercase letter")
    if lower_avail:
        print("The password is strong.It contains one or more lowercase letters")
    else:
        print("The password is weak.It must have at least one lowercase letter")
       
    if digit_avail:
        print("The password is strong.It contains one or more digits")    
    else:
        print("The password is weak.It must contain at least one digit")
    if special_avail:
        print("The password is strong.It contains one or more special characters")    
    else:
        print("The password is weak.It must contain at least special character")
passwordStrengthChecker(password)