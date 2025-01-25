total_bill=float(input("enter the total bill amount"))
number_of_people=int(input("enter the number of people"))
tip_percentage=float(input("enter the tip percentage"))
tip_amount=(total_bill*tip_percentage)/100
bill_split=(total_bill+tip_amount)/number_of_people
print(f"the split is{bill_split}")

