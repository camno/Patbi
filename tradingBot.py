import asyncio 
from ib_insync import IB, util, Contract, MarketOrder


class TradingBot:

    def __init__(self):
        # Creates an instance of the IB client class
        self.ib = IB()
        self.current_price = None

    async def connect(self):

        util.startLoop()
        self.ib.connect('127.0.0.1', 7497, clientId=1)
        while not self.ib.isConnected():
            await asyncio.sleep(0.1)

    async def request_price(self, contract):
        tickers = self.ib.reqTickers(contract)
        self.current_price = tickers[0].marketPrice()


    async def request_realtime_bars(self, contract,):
    # barSize must be 5
    # If True then only show data from within Regular Trading Hours(RTH), 
    # if False then show all data.
        bars = await self.ib.reqRealTimeBars(
            contract, 
            barSize = 5, # real time bar size in seconds, and it must be 5
            whatToShow = 'TRADES', 
            useRTH = False)
        
        # bars.updateEvent += onBarUpdate

    
        return bars

    async def place_order(self, contract, order):
        self.ib.placeOrder(contract, order)

    async def trade(self, contract, order):
        await self.request_price(contract)
        await self.place_order(contract, order)

    
    # def onBarUpdate(bars, hasNewBar):
    #     print(bars[-1])

    def stop(self):
        self.ib.disconnect()

