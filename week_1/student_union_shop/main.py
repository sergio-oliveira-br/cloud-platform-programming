# week_1/student_union_shop/main.py

from week_1.student_union_shop.store.products import Item, Cap, Shirts, Hoodie


# Problem 3: You have been asked to create an
# application for the Student Union shop which sells
# caps for 5, shirts for 10 and hoodies for 20. Your
# application should allow the user to input the quantity
# of each item a student wants to buy and then
# calculate and output the total cost. When you have
# finished the implementation, test your application to
# ensure that the calculations are correct.


def main():
    print("\n***Welcome to Student Union Shop!***")

    product = input("\nWhich product would you like to buy?"
          "\n1. Cap - €5 "
          "\n2. Shirt - €10"
          "\n3. Hoddie - €20\n")


    if product == "1":
        quantity = int(input("\n@Cap selected. \n-> Please enter the quantity you would like to buy.\n"))
        total_price = Cap().calculate_total_cost(quantity)
        print("\nYour total cost is €{:.2f}.".format(total_price))

    elif product == "2":
        quantity = int(input("\n#Shirt selected. \n-> Please enter the quantity you would like to buy.\n"))
        total_price = Shirts().calculate_total_cost(quantity)
        print("\nYour total cost is €{:.2f}.".format(total_price))

    elif product == "3":
        quantity = int(input("\n$Hoddie selected. \n-> Please enter the quantity you would like to buy.\n"))
        total_price = Hoodie().calculate_total_cost(quantity)
        print("\nYour total cost is €{:.2f}.".format(total_price))

    else:
        raise ValueError("Invalid input. Please enter a valid input.")

if __name__ == "__main__":
    main()



