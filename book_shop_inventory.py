"""

"""

current_inventory = [
    "vampires of el norte", "the pirate queen",
    "the witch", "the haunting of hill house", 
    "mexican gothic", "frankenstein", 
    "dracula"
]

book_price = {
    "vampires of el norte": 15,
    "the pirate queen": 20,
    "the witch": 30,
    "the haunting of hill house": 20,
    "mexican gothic": 20,
    "frankenstein": 10,
    "dracula": 30
}

print(f"\nWelcome to the book shop! Please take a look at "
      "our inventory:")

for book in current_inventory:
    print(book.title())

customer_order = []
ordering_book = True


# Customer ordering system
print(f"\nPlease input the books you would like to buy, one at a time.")
print("Enter 'quit' when you are done: ")

while ordering_book:
    book_choice = input("Book name: ")
    book_choice = book_choice.lower()

    if book_choice in current_inventory:
        customer_order.append(book_choice)
        current_inventory.remove(book_choice)

    elif book_choice == 'quit':
        ordering_book = False
        print("\nThe following books have been added to your cart:")

        for order in customer_order:
            print(order.title())

    else:
        print(f"\nSorry, we don't have that book. Please enter a book from our inventory.")


# Calculating order total
order_total = 0

for order in customer_order:
    order_total += book_price[order]

# Calculating discount
user_age = input(f"\nPlease enter your age: ")
user_age = int(user_age)

if user_age <= 12:
    order_total -= 10
    print(f"\nYou got $10 off! Your order total is ${order_total}.")
elif user_age >= 65:
    order_total -= 5
    print(f"\nYou got $5 off! Your order total is ${order_total}.")
else:
    print(f"\nYour order total is ${order_total}.")

