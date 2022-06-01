class StockStateMachine:
    STATUS_START = 'START'
    STATUS_BUY = 'BUY'
    STATUS_SELL = 'SELL'
    STATUS_SELL_HOLD = 'SELLHOLD'
    STATUS_END = 'END'

    def __init__(self, threshold, average):
        self.threshold = threshold
        self.state = "START"
        self.stock_price = 0
        self.stock_bought_price = 0
        self.average = average
        self.is_bought = False

    def is_stock_cheap(self):
        return self.stock_price < self.average

    def is_stock_at_loss(self):
        stock_reduced = self.stock_bought_price - (self.stock_bought_price * self.threshold)
        return self.stock_price < stock_reduced

    def is_stock_at_win(self):
        stock_increased = self.stock_bought_price + (self.stock_bought_price * self.threshold)
        return self.stock_price > stock_increased

    def next_state(self):
        if self.is_stock_cheap() and self.state == self.STATUS_START:
            self.state = self.STATUS_BUY
            self.is_bought = True
            self.stock_bought_price = self.stock_price
        elif self.is_bought and self.state == self.STATUS_BUY:
            self.state = self.STATUS_SELL_HOLD
        elif (self.is_stock_at_loss() or self.is_stock_at_win()) and self.state == self.STATUS_SELL_HOLD:
            self.state = self.STATUS_SELL
        elif self.state == self.STATUS_SELL:
            self.state = self.STATUS_END

    def get_state(self):
        return self.state
