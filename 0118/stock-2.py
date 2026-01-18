import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# 1. 設定參數
stock_id = "2330.TW"  # 股票代號
period = "1y"         # 時間範圍：1年

print(f"正在下載 {stock_id} 的資料...")

# 2. 下載資料
ticker = yf.Ticker(stock_id)
df = ticker.history(period=period)

# 3. 計算移動平均線 (Moving Average)
# 使用 rolling().mean() 來計算滾動平均值
# MA20 (月線)：代表過去 20 個交易日的平均成本，常用於看短期趨勢
df['MA20'] = df['Close'].rolling(window=20).mean()

# MA60 (季線)：代表過去 60 個交易日的平均成本，常用於看中期趨勢 (生命線)
df['MA60'] = df['Close'].rolling(window=60).mean()

# 4. 繪製圖表
plt.figure(figsize=(12, 6)) # 設定圖表大小

# 畫收盤價 (半透明黑色，以免擋住均線)
plt.plot(df.index, df['Close'], label='Close Price', color='black', alpha=0.3)

# 畫 MA20 (橘色)
plt.plot(df.index, df['MA20'], label='MA20 (Monthly)', color='orange', linewidth=2)

# 畫 MA60 (綠色)
plt.plot(df.index, df['MA60'], label='MA60 (Quarterly)', color='green', linewidth=2)

# 圖表設定
plt.title(f"{stock_id} Stock Price & Moving Averages")
plt.xlabel("b4")
plt.ylabel("Price (TWD)")
plt.legend() # 顯示圖例
plt.grid(True) # 顯示格線

# 顯示圖表
plt.show()