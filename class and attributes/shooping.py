class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, items, price, quantity):
        products = {'items ': items, 'price' : price, 'quantity': quantity }
        self.cart.append(products)

    def checkout(self,amount):
        total = 0
        for iteam in self.cart:
            print(iteam)
            total += iteam['quantity'] * iteam['price']
        print('the Total price : ', total)

        if amount < total:
            print('You donot provide enough money')
            print(f'Please provide me {amount-total}')
        else:
            extra = amount - total
            print(f'you will get return {extra}')

            
Ayon = Shop('Ayon')
Ayon.add_to_cart('Whey Protein', 350, 1)
Ayon.add_to_cart('Meat', 22, 1)
Ayon.add_to_cart('Eggs', 3.5, 10)
print(Ayon.cart)

Ayon.checkout(1000)