# ==========================================
# 第一步：匯入需要的工具箱 (Libraries)
# ==========================================
import yfinance as yf       # 用來從網路上下載股票數據的工具
import mplfinance as mpf    # 專門用來畫金融 K 線圖 (蠟燭圖) 的工具

# ==========================================
# 第二步：設定參數 (這裡是控制台，改這裡就好)
# ==========================================
stock_id = "5701.TWO"        # 股票代號 (台股記得要加 .TW)
start_date = "2023-10-01"   # 資料開始日期
end_date   = "2024-01-01"   # 資料結束日期
filename = "my_stock_chart.png" # 存檔的圖片名稱

print(f"請稍等，正在下載 {stock_id} 的資料...")

# ==========================================
# 第三步：下載資料
# ==========================================
# yf.download 會回傳一個表格 (DataFrame) 給我們
df = yf.download(stock_id, start=start_date, end=end_date)

# ==========================================
# 第四步：資料清理 (Data Cleaning) ★這段最重要★
# ==========================================
# 最近 yfinance 更新了，下載回來的表格標題會有「兩層」(MultiIndex)
# 例如： ('Close', '2330.TW')
# 畫圖軟體看不懂兩層標題，所以我們要幫它「脫掉一層外衣」

# 檢查：如果欄位標題真的是多層索引...
# if isinstance(df.columns, pd.MultiIndex):
    # 就把第 1 層 (也就是股票代號那一層) 刪掉，只保留 Open, High, Low...
df.columns = df.columns.droplevel(1)

# 確保：把表格內所有資料強制轉成「浮點數 (小數點數字)」
# 這是為了避免電腦誤判資料是「文字」，導致無法畫圖
# astype(float) 就是 "As Type Float" 的縮寫
df = df.astype(float)

# ==========================================
# 第五步：設定圖表外觀
# ==========================================
# 台灣股市習慣：紅色是漲 (Up)，綠色是跌 (Down)
# 美國股市習慣相反，所以我們要特別設定
my_color = mpf.make_marketcolors(up='r', down='g', inherit=True)
my_style = mpf.make_mpf_style(marketcolors=my_color)

# ==========================================
# 第六步：繪製並存檔
# ==========================================
print(f"資料處理完畢，正在繪製圖表並存檔...")

mpf.plot(
    df,                  # 要畫的資料表格
    type='candle',       # 圖表類型：candle 代表蠟燭圖 (K線)
    style=my_style,      # 使用我們剛剛設定的紅漲綠跌樣式
    volume=True,         # 是否要顯示下方的成交量 (Volume)
    title=f"{stock_id} K-Chart", #圖片上方的標題
    figsize=(12, 6),     # 圖片大小 (寬, 高)
    savefig=filename     # 直接存成圖片檔案，不跳出視窗
)

# print(f"圖表已經畫好並存成 {filename} 了！")