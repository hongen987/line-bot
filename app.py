from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('OjH+fIAI+bRqJdLWWtaTzZHuRD+jbCwfkYQKW0U3wL2On5Vl2X8jISUdlCt3BHe1eVIKDiKLMw9dzT+MoS+6LiupOPtqhTTvEOaaGX/ql2neGeedFvoAFC9vGxlLVNqBTBO1IHzg5TKfkvPbVl12TgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('015d1f0590649482eda9a982f805979b')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    rp = event.message.text
    if '貼圖' in rp:
        StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=))


if __name__ == "__main__":
    app.run()