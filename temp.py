#c-f
def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5)+32
#c-k
def celsius_to_kelvin(celsius):
    return celsius + 273.15
#f-c
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
#f-k
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit-32)*5/9 +273.15
#k-c
def kelvin_to_celsius(kelvin):
    return kelvin-273.15
#k-f
def kelvin_to_fahrenheit(kelvin):
    return (kelvin-273.15)*9/5+32

while True:
    print("1. Celsius to Fahrenheit \n2. Celsius to Kelvin \n3. Fahrenheit to Celsius \n4. Fahrenheit to Kelvin \n5. Kelvin to Celsius \n6. Kelvin to Fahrenheit \n7. Exit")
    choice = int(input("Choose a number between (1-7): "))
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_kelvin(celsius):.2f} K")
    elif choice == 3:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    elif choice == 4:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit):.2f} K")
    elif choice == 5:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} K = {kelvin_to_celsius(kelvin):.2f}°C")
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} K = {kelvin_to_fahrenheit(kelvin):.2f}°F")
    elif choice == 7:
        break
    else:
        print("Invalid choice. Select a valid option.")