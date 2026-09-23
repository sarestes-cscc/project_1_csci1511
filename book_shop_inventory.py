"""

"""


# Have current inventory in the form of a dictionary,
#   keys will be genre, and values will be lists with 
#   the book names

# Have a series of events that add or remove 
#   books from inventory

# Have a discount system for seniors and kids using if statements

# Use a for loop to print the names of the current 
#   inventory by genre

# Use a while loop to update list

# Include user input

current_inventory = [
    "vampires of el norte", "the pirate queen",
    "the witch", "the haunting of hill house", 
    "mexican gothic", "frankenstein", 
    "dracula"
]


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
    customer_order.append(book_choice)

    if book_choice == 'quit':
        ordering_book = False
        customer_order.remove("quit")
        print("\nThe following books have been added to your cart:")

        for order in customer_order:
            print(order.title())


# Calculating order total
order_total = 0

for order in customer_order:
    order_total += 25

# Calculating discount
user_age = input(f"\nPlease enter your age: ")
user_age = int(user_age)

if user_age <= 12:
    order_total -= 10
if user_age >= 65:
    order_total -= 5


print(f"\n Your order total is ${order_total}.")
print("\nThank you! Please come again.")

