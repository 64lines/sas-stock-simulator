import random
import time
import json

def generate_stock_price(stock_price):
  return stock_price + random.randint(-2, 2)
  
def simulation():
  account_balance = 10000
  stock_price = 300
  threshold = 0.5
  stocks = []
  buy_price = 0

  stock = { "name": "TSLA", "price": generate_stock_price(stock_price), "average": 250}
  stock_name = stock["name"]
  stock_price = stock["price"] 
  stock_average = stock["average"]
  is_first_time = True

  while True:
    # Load configuration
    json_file = open('config.json', 'r')
    data = json.load(json_file)
    json_file.close()

    stock_price += random.randint(1, 50) if data['increase'] else random.randint(-50, 1)
    # Show price
    if stocks:
      percentage_value = ((stock_price - buy_price) * 100) / buy_price
      percentage = '\033[0;31m{0:.3g}%\033[0m'.format(percentage_value) if percentage_value < 0 else '\033[0;32m{0:.3g}%\033[0m'.format(percentage_value)
      print('Stock price: \033[0;36m${}\033[0m, Average: ${}, Stocks: [{}: {}] {}, Invested: $ {}'.format(stock_price, stock_average, stock_name, stock_price, percentage, buy_price))
    else:
      print('Stock price: \033[0;36m${}\033[0m, Average: ${}'.format(stock_price, stock_average))

    is_a_buy = buy(stock_price, stock_average)
    is_a_sell = sell(buy_price, stock_price, threshold)

    # Sell
    if is_a_sell and stocks:
      print('\033[0;35m[S] -- Sell stock: {} for ${}\033[0m'.format(stock_name, stock_price))
      account_balance += stock_price
      stocks = []
      print('\033[0;35m    -- Account balance: ${}'.format(account_balance))
      print('\033[0;35m    -- Stocks: [] \033[0m')
    
    # Buy
    if is_a_buy and is_first_time:
      print('\033[0;36m[B] -- Buy stock: {} \033[0m'.format(stock_name))
      account_balance -= stock_price
      buy_price = stock_price
      stocks.append(stock_name)
      print('\033[0;36m    -- Account balance: ${}\033[0m'.format(account_balance))
      print('\033[0;36m    -- Stocks: [{}: {}] \033[0m'.format(stock_name, buy_price))
      is_first_time = False

    
    
    # Sleep 1 second
    time.sleep(2)

def sell(buy_price, stock_price, threshold):
  # 10% of the bought price
  buy_price_percentage = buy_price * threshold

  if buy_price and stock_price > buy_price + buy_price_percentage:
    return True
  
  if buy_price and stock_price < buy_price - buy_price_percentage:
    return True
  
  return False

def buy(stock_price, average):
  if stock_price < average:
    return True
  
  return False

def run_simulation():
  try:
    simulation()
  except Exception as e:
    print(e)
  

run_simulation()