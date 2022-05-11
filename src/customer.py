class Customer:
    
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkenness = 0

    def decrease_wallet(self, price):
        self.wallet -= price
    
    def increase_drunkenness(self, alcohol):
        self.drunkenness += alcohol

    def customer_buys_drink(self, drink):
        self.decrease_wallet(self, drink)
        self.increase_drunkenness(self, drink)
        
            
       

    # def test_customer_can_buy_drink(self):
    #     drink = Drink

