import asyncio
from ib_insync import IB, util, Contract, MarketOrder
from tradingBot import *


async def main():
    bot = TradingBot()
    await bot.connect()

    contract = Contract(symbol = ticker_name, secType='STK', exchange='SMART', currency='USD')
    order = MarketOrder('BUY', 100)
    await bot.trade(contract, order)

if __name__ == "__main__":
    with open('trading_stock.txt', "r") as f:
        args = f.read().splitlines()
    asyncio.run(main(ticker_name = args[0]))