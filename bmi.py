weight=float(input('enter the weight in kgs'))
height=float(input("enter the height in meters"))
bmi=weight/height
if bmi<18.5:
    print('Underweight')
elif bmi>18.5 or bmi<25:
    print("Normal Weight")
elif bmi>25 or bmi<30:
    print('overweight')
elif bmi>=30:
    print('Obese')

