class Account:
    def __init__(self, *, firstname, lastname, number, balance=None):
        assert isinstance(number, int), 'Number needs to be an integer'
        if balance is not None:
            assert isinstance(balance, float), 'Balance needs to be a float'
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance or 0.0

    def info(self):
        # Number 1: Albert Einstein - 100.0 €'
        return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def has_funds_for(self, amount):
        return self.balance > amount



    def add_to_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        self.balance += amount


    def subtract_from_balance(self, amount):
        assert self.balance > amount, 'Account has not enough funds'
        self.balance -= amount















