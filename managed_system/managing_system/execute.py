from managed_system.managing_system.state_machine import StockStateMachine
from managed_system.model import Stock

class StockActioner:
    def __init__(self, stock_name, account, controller):
        self.account = account
        self.stock_name = stock_name
        self.controller = controller

    def perform_action(self, stock_price, state):
        stock = Stock(name=self.stock_name, price=stock_price)
        if state == StockStateMachine.STATUS_BUY:
            self.controller.buy_stock(stock, self.account)
            print(self.account.get_portfolio())
        elif state == StockStateMachine.STATUS_SELL:
            self.controller.sell_stock(stock, self.account)
            print(self.account.get_portfolio())
        