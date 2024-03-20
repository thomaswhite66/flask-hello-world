from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    # print(json_data)
    try:
        line_bot_api = LineBotApi('你的 LINE Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']                 # 取得 reply token
        msg = json_data['events'][0]['message']['text']           # 取得使用者發送的訊息
        print(f'使用者傳送訊息: {msg}')                             # 印出使用者發送的訊息
        # line_bot_api.reply_message(tk, TextSendMessage(text=msg)) # 回傳訊息(目前單純重複使用者的訊息)
    except Exception as e:
        print(f"捕獲到異常：{type(e).__name__}: {str(e)}")
    return 'OK'

if __name__ == "__main__":
    app.run()