class Category:
    def __init__(self,name) -> None:
        self.name = str(name)
        self.ledger = list()

    def __str__(self) -> str:
        name = self.name
        distance = int((30-len(name))/2)
        description = f"{(distance*'*')}{name}{(distance*'*')}"
        ledger_items = str()
        for obj in self.ledger:
            shortened_description = obj['description'][:(29-len(str(obj['ammount'])))]
            
            spaces = f"{(30-(len(shortened_description)+len(str(obj['ammount']))))*' '}"
            ledger_items+=f"{shortened_description}{spaces}{obj['ammount'] if isinstance(obj['ammount'],float) else str(obj['ammount'])+'.00'}\n"
        return f"{description}\n{ledger_items}"

    def deposit(self,ammount:int,description=""):
        self.ledger.append({"ammount":ammount,"description":description})
    
    def get_balance(self) -> int:
        total = 0
        for obj in self.ledger:
            total += obj["ammount"]
        return total
    
    def check_funds(self,ammount) -> bool:
        return self.get_balance() > ammount
    
    def withdraw(self,ammount:int,description=""):
        if not self.check_funds(ammount):
            return False
        self.ledger.append({"ammount":-ammount,"description":description})
        return True
    
    
    def transfer(self,ammount,category):
        is_valid = self.check_funds(ammount)
        if not is_valid:
            return False
        if is_valid:
            self.withdraw(ammount,f'Transfer to {self.name}')
            category.deposit(ammount,f'Transfer from {category.name}')
        return True


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
print(food)
expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
print(expected)
# def create_spend_chart(categories):

"""
f"
*************Food*************
deposit                 900.00
milk, cereal, eggs, bac -45.67
Transfer to Entertainme -20.00
Total: 834.33"
"""