import requests
import json

# ================= 設定區 =================
# 1. 剛剛發行的 Channel Access Token (長的那串)
TOKEN = "T3zoTOT60e7F+k6Wm0mOHy/Y7ckRJrfPgpZZjrYIGTKror7KhIVY5wNAicahyv4jX/Uz683W8n/DzYvVCDG9K0hPmpUqFuF4PQ5S/1iTSrs7Z/ZSgHYaR6Vj4YOZMWcHbJnTSmvh+w11T3ZkaOgzWAdB04t89/1O/w1cDnyilFU="

# 2. 你的 User ID (U開頭的那串)
USER_ID = "U0547321a842dadf0805790b9cb6aa845"

# =========================================

text = "嘿嘿嘿!"

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
