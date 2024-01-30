class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self.customer = customer
        self.bank = bank
        self.acnt = acnt
        self.limit = limit
        self.balance = balance

    def get_cutsomer(self):
        return self.cutsomer
    def get_bank(self):
        return self.bank
    def get_account(self):
        return self.account()
    def get_limit(self):
        return self.lmiti()
    def get_balance(self):
        return self.balance

    def charge(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price can't be negative")
        if price + self.balance > self.limit:
            print(f"Charge can't be made, you're over the limit {self.customer}")
            return False
        else:
            self.balance += price
        return True

    def make_payment(self, amount):
        self.balance -= amount