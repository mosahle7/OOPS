from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("My ItemKeyBoard",7589)
item1.name="Other"

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.send_email())
 
print(item1.name)
print(item1.price) 
Item.instantiate_from_csv()

# print(Item.all)


# print(Item.is_integer(7.0))


# phone1 = Phone('jscPhonev18', 4000, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone('jscPhonev20', 4999, 9,2)
# # Item.instantiate_from_csv()
# # print(Item.all)
# print(Item.all)
# print(Phone.all)
        
        
# print(item1.quantity)
# print(item1.calculate_total_price())

# print(type(item1))



# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.pay_rate)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.price)



# for inst in Item.all:
#     print(inst.__dict__)


# item1 = 'Phone'
# item1_price=5000
# item1_quantity=5
# item1_price_total = item1_price*item1_quantity

# print(type(item1))
# print(type(item1_price_total))