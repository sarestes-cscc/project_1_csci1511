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
