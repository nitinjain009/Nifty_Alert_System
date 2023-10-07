import datetime
import yfinance as yf
from telegram_bot import nifty_alert   

nifty = "^NSEI"
ticker = yf.Ticker(nifty)
wk_52_low = ticker.info['fiftyTwoWeekLow']
wk_52_high = ticker.info['fiftyTwoWeekHigh']


# View the ticker.info dict 
# ticker_info = ticker.info
# for key,value in ticker_info.items():
#     print(key," : ",value)

history = ticker.history(period="1y")

low = round(history['Low'].iloc[-1], 2)
high = round(history['High'].iloc[-1], 2)

prev_low = round(history['Low'].iloc[-2], 2)
prev_high = round(history['High'].iloc[-2], 2)

ma_50_list = history['Close'].rolling(window=50).mean()
ma_50 = round(ma_50_list.iloc[-1], 2)
prev_ma_50 = round(ma_50_list.iloc[-2], 2)

ma_100_list = history['Close'].rolling(window=100).mean()
ma_100 = round(ma_100_list.iloc[-1], 2)
prev_ma_100 = round(ma_100_list.iloc[-2], 2)

ma_200_list = history['Close'].rolling(window=200).mean()
ma_200 = round(ma_200_list.iloc[-1], 2)
prev_ma_200 = round(ma_200_list.iloc[-2], 2)

########## Alert Function #############

def nifty_cross_alert(prev_low, prev_high, low, high, prev_ma_50, prev_ma_100, prev_ma_200, ma_50, ma_100, ma_200, ):
    #check 50 MA cross over
    if (prev_low >= prev_ma_50) and (low <= ma_50):
        nifty_alert("Nifty has crossed 50 MA from above", "fall")
        return
    elif (prev_high <= prev_ma_50) and (high >= ma_50):
        nifty_alert("Nifty has crossed 50 MA from below", "rise")
        return
    #check 100 MA cross over
    elif (prev_low >= prev_ma_100) and (low <= ma_100):
        nifty_alert("Nifty has crossed 100 MA from above", "fall")
        return
    elif (prev_high <= prev_ma_100) and (high >= ma_100):
        nifty_alert("Nifty has crossed 100 MA from below", "rise")
        return
    #check 200 MA cross over
    elif (prev_low >= prev_ma_200) and (low <= ma_200):
        nifty_alert("Nifty has crossed 200 MA from above", "fall")
        return
    elif (prev_high <= prev_ma_200) and (high >= ma_200):
        nifty_alert("Nifty has crossed 200 MA from below", "rise")
        return


def is_close_to_52_week_low(low, fifty_two_week_low):
    percentage_difference = fifty_two_week_low + fifty_two_week_low * (1 / 10)
    if (low <= percentage_difference):
        nifty_alert("Nifty is just 10% away from 52 week low", "fall")
        return
 
    
def is_close_to_52_week_high(high, fifty_two_week_high):
    percentage_difference = fifty_two_week_high - fifty_two_week_high * (1 / 10)
    if high >= percentage_difference:
        nifty_alert("Nifty is just 10% away from 52 week high", "rise")
        return

today = datetime.date.today()
if today.weekday() < 6:    
    nifty_cross_alert(prev_low, prev_high, low, high, prev_ma_50, prev_ma_100, prev_ma_200, ma_50, ma_100, ma_200)
    is_close_to_52_week_low(low, wk_52_low)
    is_close_to_52_week_high(high, wk_52_high)
 

########### Code End ############ 