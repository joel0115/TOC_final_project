import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def push_text_message(id, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TextSendMessage(text=text))


def send_flex_message(id, content):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, FlexSendMessage(
        alt_text="Error happened when sending flex message.", contents=content))


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
