import time
from managed_system.managing_system.execute import StockActioner
from managed_system.managing_system.state_machine import StockStateMachine
from managed_system.model import Account, Stock

class Monitor:
    STOCK_PRICE = 100
    INCREASE_MODE = 'INCREASE'
    DECREASE_MODE = 'DECREASE'

    def __init__(self, stock: Stock, state_machine: StockStateMachine, mode, controller):
        self.stock = stock
        self.state_machine = state_machine
        self.mode = mode
        self.controller = controller
        self.stock_price = stock.price

    def listen(self):
        account = Account(10000)
        actioner = StockActioner(
            stock_name=self.stock.name, 
            controller=self.controller,
            account=account
        )

        while True:
            print('{} - ${}'.format(self.stock.name, self.stock_price))
            self.state_machine.stock_price = self.stock_price
            self.state_machine.next_state()
            current_state = self.state_machine.get_state()

            print('State: ', current_state)
            actioner.perform_action(state=current_state, stock_price=self.stock_price)
            
            if self.mode == self.INCREASE_MODE:
                self.stock_price += 1
            elif self.mode == self.DECREASE_MODE:
                self.stock_price -= 1

            time.sleep(1)