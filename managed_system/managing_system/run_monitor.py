from state_machine import StockStateMachine
from monitor import Monitor

stocks_state_machine = StockStateMachine(threshold=0.5, average=90)
Monitor(
    state_machine=stocks_state_machine, 
    mode=Monitor.DECREASE_MODE
).listen()