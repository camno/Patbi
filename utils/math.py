import numpy as np 
import pandas as pd
from const import *

def calc_share_quantity(entry_price, stop_loss_price, equity_balances):

    # R is the maxmum loss for a position
    R = max_risk * equity_balances
    shares = min(4 * equity_balances // entry_price, R // (entry_price - stop_loss_price))

    return shares

