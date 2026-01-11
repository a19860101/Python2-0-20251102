import yfinance as yf
# pip install yfinance

tsmc = yf.Ticker("0050.TW")
hist = tsmc.history(period="1mo")
print(hist)