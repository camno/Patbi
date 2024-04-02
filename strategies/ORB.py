import pandas as pd 
import numpy as np
from ib_insync import Stock
from utils import *
from asyncio import *

def orb_five_mins():
    print("success!!")

def get_TS_long_contracts():
    # Request details for TQQQ and SQQQ contracts
    tqqq_contract = Stock("TQQQ", exchange = "ISLAND")
    sqqq_contract = Stock("SQQQ", exchange = "ISLAND")

    return tqqq_contract, sqqq_contract

async def real_time_trading(ib_client, bars):
    for bar in bars:
        print(f"Received real-time bar:{bar}")

        # check if the price satisfies the trade condition