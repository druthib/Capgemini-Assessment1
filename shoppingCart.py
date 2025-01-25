def add_item(cart):
    item_name=input("Enter the item name: ")
    item_price=float(input(f"Enter the price for {item_name}: "))
    cart.append({"name": item_name, "price": item_price})
    print(f"{item_name} has been added to your cart")
def view_cart(cart):
    if not cart:
        print("Your cart is empty")
    else:
        print("Items in your cart:")
        for item in cart:
            print(f"{item['name']} - {item['price']:.2f} Rs")
def calculate_total(cart):
    total=sum(item['price'] for item in cart)
    print(f"Total price: {total:.2f} Rs")
def exit():
    print("Thank you for shopping!")
    return 1
def shopping_cart():
    cart=[]
    while True:
        print("1.Shopping cart menu \n2.View cart \n3.Calculate total price \n4.Exit") 
        choice=int(input("Enter your choice: "))
        if choice == 1:
            add_item(cart)
        elif choice == 2:
            view_cart(cart)
        elif choice == 3:
            calculate_total(cart)
        elif choice == 4:
            exit()
            break
        else:
            print("Invalid choice. Please choose a valid option") 
        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes':
            print('Exiting the program.')
            break
shopping_cart()