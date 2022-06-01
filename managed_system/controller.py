from managed_system.managing_system.state_machine import StockStateMachine
from managed_system.model import Account, Stock
from managed_system.managing_system.monitor import Monitor
from managed_system.managing_system.knowledge import STOCK_METADATA

class StockController:
    def buy_stock(self, stock: Stock, account: Account):
        stock.buy(account)

    def sell_stock(self, stock: Stock, account: Account):
        stock.sell(account)

class StockSensor:
    def sense_price(self, stock):
        stocks_state_machine = StockStateMachine(
            threshold=STOCK_METADATA['threshold'],
            average=STOCK_METADATA['average']
        )
        Monitor(
            stock=stock,
            controller=StockController(),
            state_machine=stocks_state_machine, 
            mode=Monitor.DECREASE_MODE
        ).listen()