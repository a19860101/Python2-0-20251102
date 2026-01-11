import yfinance as yf
# pip install yfinance

tsmc = yf.Ticker("2330.TW")
# 查詢歷史紀錄
# m：分鐘
# d：日
# mo：月
# y：年
# hist = tsmc.history(period="2d")
# interval區間
data = tsmc.history(period='3mo')

# 收盤價
# print(data['Close'])

# 5日均線
data['MA5'] = data['Close'].rolling(window=5).mean()
# 30日均線
data['MA30'] = data['Close'].rolling(window=30).mean()
# 60日均線
data['MA60'] = data['Close'].rolling(window=60).mean()

print(data['MA5'])
print(data['MA30'])
print(data['MA60'])
