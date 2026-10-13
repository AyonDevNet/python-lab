
class Shop:
    #cart = [] #this is class attribute, share all the things we each others
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, items):
        self.cart.append(items)


customer1 = Shop('Ayon')
customer1.add_to_cart('Shoes')
customer1.add_to_cart('Gaming Controller')
customer1.add_to_cart('Keyboard')

print(customer1.buyer)
print(customer1.cart)


customer2 = Shop('Rafi')
customer2.add_to_cart('T-shirt')
customer2.add_to_cart('Pant')
customer2.add_to_cart('Watch')

print(customer2.buyer)
print(customer2.cart)
