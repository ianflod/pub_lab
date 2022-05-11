class Pub:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, price):
        self.till += price

    # def serve(self, customer, drink):
    #     if self.drinks.count(drink) ==0:
    #         return

