from item import Item

class Phone(Item):
    pay_rate=0.5
    
    def __init__(self,name: str, price: float, quantity=0,broken_phones=0):
        # call to super function to have access to all attributes n methods
        super().__init__(
            name, price, quantity
        )
        # run validations to received arguments
        assert broken_phones>=0, f"Quantity can't be negative, {broken_phones} rejected!"
    
        # assign to self object
        self.broken_phones=broken_phones
        
        # actions to execute
        # Phone.all.append(self)
