from managed_system.controller import StockSensor
from managed_system.model import Stock

if __name__ == "__main__":
    try:
        stock = Stock(name='APPL', price=100)
        StockSensor().sense_price(stock=stock)
    except:
        pass