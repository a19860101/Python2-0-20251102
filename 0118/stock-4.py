# ==========================================
# 第一步：匯入需要的工具箱
# ==========================================
import yfinance as yf
import mplfinance as mpf

# ==========================================
# 第二步：設定參數
# ==========================================
stock_id = "0050.TW"  # 股票代號
start_date = "2023-10-01"  # 開始日期
end_date = "2024-01-01"  # 結束日期
filename = "tsmc_ma_chart.png"  # 存檔名稱

print(f"請稍等，正在下載 {stock_id} 的資料...")

# ==========================================
# 第三步：下載資料
# ==========================================
df = yf.download(stock_id, start=start_date, end=end_date)

# ==========================================
# 第四步：資料清理 (Data Cleaning) ★重要★
# ==========================================
# 處理 yfinance 新版格式問題，把多餘的標題層級刪掉
# if isinstance(df.columns, pd.MultiIndex):
df.columns = df.columns.droplevel(1)

# 強制轉為數字格式
df = df.astype(float)

# ==========================================
# 第五步：設定圖表外觀
# ==========================================
# 設定台股習慣：紅漲 (Up) 綠跌 (Down)
my_color = mpf.make_marketcolors(up='r', down='g', inherit=True)
my_style = mpf.make_mpf_style(marketcolors=my_color)

# ==========================================
# 第六步：繪製包含「均線」的圖表
# ==========================================
print(f"正在繪製 K 線與均線...")

mpf.plot(
    df,
    type='candle',  # 畫 K 線
    style=my_style,  # 套用紅漲綠跌
    volume=True,  # 顯示成交量
    title=f"{stock_id} K-Chart with MA",
    figsize=(12, 6),
    # savefig=filename,  # 存檔

    # mav 代表 Moving Average (移動平均線)
    # (5, 20) 代表要畫出「5日均線」和「20日均線」
    mav=(5, 20)
)

# print(f"圖表已畫好，包含 5日與20日均線，存檔為 {filename}")