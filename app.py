#載入LineBot所需要的模組 
from flask import Flask, request, abort  
from linebot import (
    LineBotApi, WebhookHandler
 ) 
from linebot.exceptions import (
    InvalidSignatureError
 ) 
from linebot.models import *

app = Flask(__name__)  
# 必須放上自己的Channel Access Token 
line_bot_api = LineBotApi('mvwVq2sJsehGFk4S+EcZZIE+iiiz84X75F25OmzbBAWmN38CSS9b0peFsnyo/pVZmelWV7FKo+0idSInWPFIhB/FKEurySO72fRnW4qifQhS1B1JvoJSBGSFpDqqqKBcsSYCPDRV5ToZUslzdGg4eAdB04t89/1O/w1cDnyilFU=')  
# 必須放上自己的Channel Secret
handler = WebhookHandler('db6a92064c543b1380b52c8eab14d646')  

line_bot_api.push_message('Uba61a3d45b7acb0b333ece913cebd893', TextSendMessage(text='你可以開始了'))

#line bot與heroku串接
# 監聽所有來自 /callback 的 Post Request 
@app.route("/callback", methods=['POST']) 
def callback():     
    # get X-Line-Signature header value     
    signature = request.headers['X-Line-Signature']
    # get request body as text     
    body = request.get_data(as_text=True)     
    app.logger.info("Request body: " + body)      
    # handle webhook body     
    try:         
        handler.handle(body, signature)     
    except InvalidSignatureError:         
        abort(400)      
    return 'OK'

#訊息傳遞區塊 
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
    message = TextSendMessage(text=event.message.text)
    int(message)
    num=message
    if num >= 1000000:
        n=num /1000000
        if n%1 ==0:
            remessage=n + " million"
        else:
            remessage=n + " million"
    else:
        n=num/1000
        remessage=n+" thousand"
    line_bot_api.reply_message(event.reply_token,remessage)

#主程式 
import os 
if __name__ == "__main__":    
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)

#Wei測試串    