print("Welcome")
# functionality for cashiers
class ShoppingCart():
    items_in_cart ={}
    def __init__(self,customer_name):
        self.customer_name = customer_name

    def add_item(self,product,price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print("added "+ product)
        else:
            print(product+" is in the cart")

    def remove_item(self,product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product +"removed")
        else:
            print(product + " removed")

my_cart = ShoppingCart("Jenny")
my_cart.add_item("a computer",1200)
my_cart.add_item("a dress ",450)
my_cart.add_item("a pen ",5)
my_cart.add_item("brain ", 'priceless')
my_cart.remove_item("brain")