import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

flex_message_contents = {
    "menu": {
        "type": "bubble",
        "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "請選擇功能",
                        "align": "center",
                        "margin": "none",
                        "size": "xl"
                    }
                ],
            "backgroundColor": "#b6fc03"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "設籍問題",
                            "text": "設籍問題"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "證明文件申請流程",
                            "text": "證明文件申請流程"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "查看最新公告",
                            "text": "查看最新公告"
                        }
                    }
            ]
        }
    },

    "apply_document_menu": {
        "type": "bubble",
        "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "請選擇要申請哪類文件",
                        "align": "center",
                        "size": "lg"
                    }
                ],
            "backgroundColor": "#b6fc03"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "學生轉出",
                            "text": "學生轉出"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "成績證明",
                            "text": "成績證明"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "在學證明書",
                            "text": "在學證明書"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "中文畢業證明書",
                            "text": "中文畢業證明書"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "補辦數位學生證",
                            "text": "補辦數位學生證"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "個資異動（姓名或身分證字號）",
                            "text": "個資異動"
                        }
                    }
            ]
        }
    },

    "grade_report": {
        "type": "bubble",
        "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "申請哪種成績證明書",
                        "size": "lg",
                        "align": "center"
                    }
                ],
            "backgroundColor": "#b6fc03"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "中文成績證明書",
                            "text": "中文成績證明書"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "英文成績證明書",
                            "text": "英文成績證明書"
                        }
                    },
                {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "以上皆是",
                            "text": "以上皆是"
                        }
                    }
            ]
        }
    }
}

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
