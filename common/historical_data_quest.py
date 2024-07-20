import sys 
from ib_insync import *
import pandas as pd


def getHistoricalDate(ticker_name, 
                      duration_str, 
                      bar_size,
                      end_time):
    
    # IB connection    
    HOST = "127.0.0.1"  # defined in the IB Trader Workstation
    PORT = 7496         # defined in the IB Trader Workstation
    CLIENT_ID = 1       # defined in the IB Trader Workstation

    # util.startLoop() # Starts loop that allows us to work with the API in Jupyter notebooks – this is not necessary in a script
    ib_client = IB() # Creates an instance of the IB client class
    ib_client.connect(HOST, PORT, CLIENT_ID) # Connects to TWS

    print(ticker_name, duration_str, bar_size, end_time)

    ticker_contract = Stock(ticker_name, exchange = 'ISLAND')

    full_contract_details = ib_client.reqContractDetails(ticker_contract)

    historical_bars = ib_client.reqHistoricalData(
        ticker_contract,
        endDateTime = end_time,
        durationStr = duration_str,
        barSizeSetting = bar_size,
        whatToShow = "TRADES", # https://interactivebrokers.github.io/tws-api/historical_bars.html#hd_what_to_show
        useRTH = True, # if true, only showing regular trading hours
        formatDate = 1 # uni time stamp
    )
    df = util.df(historical_bars)
    df.to_csv('../data_output/' + ticker_name + '.csv', index = False)
    ib_client.disconnect()


if __name__ == '__main__':

    with open(sys.argv[1], "r") as f:
        args = f.read().splitlines()
    # ticker
    getHistoricalDate(ticker_name = args[0],
                      duration_str = args[1],
                      bar_size = args[2],
                      end_time = args[3]
                      )




