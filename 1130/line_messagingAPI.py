import requests
import json

# ================= 設定區 =================
# 1. 剛剛發行的 Channel Access Token (長的那串)
TOKEN = "NXG4CXoQXRIaA92OsudN9HJcu61cp/ST9EU2qUIKFudU9/gAHcjQJaNfyHN+7SNJX/Uz683W8n/DzYvVCDG9K0hPmpUqFuF4PQ5S/1iTSrv5EQ65g91NyxibhsgznlLExke8jwaEQO1Dzpy9ZFrjpwdB04t89/1O/w1cDnyilFU="

# 2. 你的 User ID (U開頭的那串)
USER_ID = "U0547321a842dadf0805790b9cb6aa845"

# =========================================

# 傳送的訊息
text = "嘿嘿嘿!"

# https://developers.line.biz/en/reference/messaging-api/#send-push-message
url = "https://api.line.me/v2/bot/message/push"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + TOKEN
}
payload = {
    "to": USER_ID,
    "messages": [{"type": "text", "text": text}]
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("成功！！")
    else:
        print(f"失敗: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"錯誤: {e}")
