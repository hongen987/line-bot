from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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
    if 'sticker' in rp:
        sticker_message = StickerSendMessage(
            package_id='6359',
            sticker_id='11069849'
        )
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='WTF'))


if __name__ == "__main__":
    app.run()