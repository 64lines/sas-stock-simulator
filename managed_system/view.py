from managed_system.model import Account, Stock
from managed_system.controller import StockController

'''
- The system should allow create an account with some money
- The system should allow you to select a stock of 3
- The system should allow you to buy and sell stocks.
- The system should show the stocks bought
- The system should show the current money
'''
class View:
    BUY_ACTION = 'b'
    SELL_ACTION = 's'
    EXIT_ACTION = 'e'
    PORTFOLIO_ACTION = 'p'
    
    def display(self):
        print("\n\t== [StockU ... The best stock broker in Medellin] ==\n")

        print("== Create an account ==")
        amount = input("[*] Account balance: ")
        account = Account(0)
        account.deposit(int(amount))

        stocks = [
            {"name": 'APPL', "price": 149 }, 
            {"name":'IBM', "price": 131}, 
            {"name":"MSFT", "price": 342}
        ]
        print("[*] What stocks do you want to buy?")
        index = 0
        for stock in stocks:
            print("   {}. {} - ${}".format(index + 1, stock["name"], stock["price"]))
            index += 1

        option = input("[*] Option: ")

        current_stock = stocks[int(option.strip()) - 1]
        stock = Stock(name=current_stock['name'], price=current_stock['price'])

        controller = StockController()
        while True:
            action = input('[*] Actions: Buy (B), Sell (S), Portfolio (P), Exit (E): ')
            if action.lower() == self.BUY_ACTION:
                controller.buy_stock(stock, account)
            elif action.lower() == self.SELL_ACTION:
                controller.sell_stock(stock, account)
            elif action.lower() == self.PORTFOLIO_ACTION:
                print('Porfolio: ', account.get_portfolio())
            elif action.lower() == self.EXIT_ACTION:
                break
