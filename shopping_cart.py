import sys
cart = []

def add_item(item):
    cart.append(item)
    print("{0} has been added".format(item))

def remove_item(item):
    try:
      cart.remove(item)
      print("{0} has been removed".format(item))
    except:
      print("Sorry")

def show_cart():
    if cart:
      print("Currently in your cart:")
      for item in cart:
        print("- {0}".format(item))
    else:
      print("Your cart is empty")

# очистка карты
def clear_cart():
    cart.clear()
    print("Your cart is empty")

def main():
    done = False
    while not done:
        answer = input(f"Please choose one of the following options? add - remove - show - clear - exit: ").lower()
        if answer == "exit":
          print("Thanks for using the program")
          show_cart()
          done = True
          sys.exit()
        elif answer == "add":
            item = input("What would you like to add? ").title()
            add_item(item)
        elif answer == "remove":
            item = input("What would you like to remove? ").title()
            remove_item(item)
        elif answer == "show":
            show_cart()
        elif answer == "clear":
            clear_cart()
        else:
            print("You did not make a valid selection")
main()