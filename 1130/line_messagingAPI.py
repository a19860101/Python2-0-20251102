import requests
import json

# ================= 設定區 =================
# 1. 剛剛發行的 Channel Access Token (長的那串)
TOKEN = ""

# 2. 你的 User ID (U開頭的那串)
USER_ID = "Ua74f123f6d1d9704a41c83bcba7e8bd8"

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
