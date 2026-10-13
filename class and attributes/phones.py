class phone:
    name = 'iphone pro'
    price = 5000
    color = 'Orange'
    brand = 'Iphone'
    feature = ['camera', 'speakers', 'gaming']



    def call(self):
        print('calling back')
        return
    def send_sms(self, sms, phones):
        text = f'send sms to {phones} and sms{sms}'
        return text
        

my_phone = phone()

# print(my_phone)
print("Brand : ", my_phone.brand)
print('color : ',my_phone.color)
print('name :' ,my_phone.name)
print('price : ' ,my_phone.price)
print('features : ' ,my_phone.feature)
my_phone.call()

print_sms = my_phone.send_sms(123232, 'i forgot to miss you')
print(print_sms)




