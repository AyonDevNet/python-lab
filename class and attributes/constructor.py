class Phone:
    manufructure = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price


my_mobile = Phone('Ayon', 'Samsung' , 500)
print(my_mobile.owner , my_mobile.brand, my_mobile.price)

her_mobile = Phone('cinthia', 'iphone' , 5500)
print(her_mobile.owner , her_mobile.brand, her_mobile.price)

dad_mobile = Phone('dady', 'iphone' , 6500)
print(dad_mobile.owner , dad_mobile.brand, dad_mobile.price)


