class Account:
    RETIRE_OP = 'RETIRE'
    DEPOSIT_OP = 'DEPOSIT'

    def __init__(self, amount):
        self.amount = amount
        self.portfolio = []

    def retire(self, value):
        self.amount -= value
        self.notify(self.RETIRE_OP, value)

    def deposit(self, value):
        self.amount += value
        self.notify(self.DEPOSIT_OP, value)
    
    def add_stock(self, stock):
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        self.portfolio.remove(self.portfolio[0])

    def get_portfolio(self):
        return [str(stock) for stock in self.portfolio]

    def notify(self, operation, value):
        print('{} - Value: ${} - Total: {}'.format(operation, value, self.amount))

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.historic_average = None
        self.selling_threshold = None

    def buy(self, account: Account):
        account.retire(self.price)
        Transaction(stock=self, operation="BUY").notify()
        account.add_stock(self)
        return True

    def sell(self, account: Account):
        Transaction(stock=self, operation="SELL").notify()
        account.deposit(self.price)
        account.remove_stock(self)
        return True

    def set_selling_threshold(self, threshold):
        self.selling_threshold = threshold

    def historic_average(self, average):
        self.historic_average = average

    def __str__(self):
        return '{}: ${}'.format(self.name, self.price)

class Transaction:
    def __init__(self, stock: Stock, operation):
        self.stock = stock
        self.operation = operation # SELL / BUY

    def notify(self):
        print('{} - {}: ${}'.format(self.operation, self.stock.name, self.stock.price))
