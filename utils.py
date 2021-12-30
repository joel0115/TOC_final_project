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
    },
    "register_question": {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "敦化國中學區",
                            "size": "xl",
                            "margin": "none",
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
                            "type": "text",
                            "text": "中華（1-19、21、22鄰）",
                            "align": "center"
                        },
                        {
                            "type": "text",
                            "text": "中正、中崙、吉仁、美仁、福成",
                            "align": "center"
                        },
                        {
                            "type": "text",
                            "text": "敦化、復源、松基（13、15-16鄰）",
                            "align": "center"
                        }
                    ]
                }
            },
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "介壽、敦化共同學區",
                            "size": "xl",
                            "margin": "none",
                            "align": "center"
                        }
                    ],
                    "backgroundColor": "#03dbfc"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "中華（20、23-25鄰）",
                            "align": "center",
                            "margin": "lg",
                            "size": "xl",
                            "offsetTop": "xxl"
                        }
                    ]
                }
            },
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "中崙、敦化共同學區",
                            "size": "xl",
                            "margin": "none",
                            "align": "center"
                        }
                    ],
                    "backgroundColor": "#fcdb03"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "復建",
                            "align": "center",
                            "margin": "lg",
                            "size": "xl",
                            "offsetTop": "xxl"
                        }
                    ]
                }
            }
        ]
    },
    "in_area_or_not": {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "請問您是否設籍在學區",
                    "size": "lg",
                    "align": "center"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "是",
                        "text": "是"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "否",
                        "text": "否"
                    }
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": []
        },
        "styles": {
            "header": {
                "backgroundColor": "#b6fc03"
            }
        }
    },
    "in_taipei_or_not": {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "是否為台北市國小畢業生？",
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
                        "label": "是",
                        "text": "是"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "否",
                        "text": "否"
                    }
                }
            ]
        }
    },
    "graduate_in_taipei": {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "自有房屋（直系二等親）",
                            "size": "xl",
                            "margin": "none",
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
                            "type": "text",
                            "text": "須符合下列條件：",
                            "offsetEnd": "none",
                            "offsetBottom": "none",
                            "margin": "none"
                        },
                        {
                            "type": "text",
                            "text": "(1)學生之直系二等親(爸爸、媽媽",
                            "align": "start",
                            "offsetTop": "md"
                        },
                        {
                            "type": "text",
                            "text": "、爺爺、奶奶、外公、外婆)在學",
                            "align": "start",
                            "offsetStart": "lg",
                            "offsetTop": "md"
                        },
                        {
                            "type": "text",
                            "text": "區內擁有房屋所有權狀，於入學前",
                            "align": "start",
                            "margin": "none",
                            "offsetStart": "xl",
                            "offsetTop": "md"
                        },
                        {
                            "type": "text",
                            "text": "一年12月31日前取得權狀(以登記",
                            "offsetStart": "xl",
                            "offsetTop": "md"
                        },
                        {
                            "type": "text",
                            "text": "日期為準)。",
                            "offsetStart": "xl",
                            "offsetTop": "md"
                        },
                        {
                            "type": "separator",
                            "margin": "lg"
                        },
                        {
                            "type": "text",
                            "text": "(2)學生與其父母或法定監護人(限",
                            "margin": "lg"
                        },
                        {
                            "type": "text",
                            "text": "單親) 於入學前一年12月31日前共",
                            "offsetStart": "xxl"
                        },
                        {
                            "type": "text",
                            "text": "同設籍於學區內。",
                            "offsetEnd": "none",
                            "offsetStart": "xxl"
                        }
                    ]
                }
            },
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "租屋",
                            "size": "xl",
                            "margin": "none",
                            "align": "center"
                        }
                    ],
                    "backgroundColor": "#03dbfc"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "須符合下列條件："
                        },
                        {
                            "type": "text",
                            "text": "(1)學生與其父母或法定監護人(限",
                            "align": "center",
                            "margin": "xxl",
                            "offsetTop": "none",
                            "offsetEnd": "lg"
                        },
                        {
                            "type": "text",
                            "text": "單親) 共同設籍於學區六年以上。",
                            "offsetStart": "xxl",
                            "margin": "xxl",
                            "offsetBottom": "xxl"
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": "(2)連續租屋且居住於學區內六年以",
                            "offsetTop": "none",
                            "margin": "xxl"
                        },
                        {
                            "type": "text",
                            "text": "上，持有經公證之房屋租賃證明。",
                            "offsetStart": "xxl",
                            "offsetTop": "none",
                            "margin": "none",
                            "offsetBottom": "xxl"
                        }
                    ]
                }
            }
        ]
    },
    "have_house_or_not": {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "是否符合自有房屋或租屋的條件？",
                    "size": "md",
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
                        "label": "是",
                        "text": "是"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "否",
                        "text": "否"
                    }
                }
            ]
        }
    },
    "determine_second_or_third": {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "backgroundColor": "#b6fc03"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "父母與學生三人共同設籍，",
                            "align": "center",
                            "margin": "xxl"
                        },
                        {
                            "type": "text",
                            "text": "若為單親須與法定監護人設籍。",
                            "align": "center"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "符合此條件",
                                "text": "第二順位"
                            }
                        }
                    ]
                }
            },
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "backgroundColor": "#03dbfc"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "父或母只有一位與學生共同設籍。",
                            "align": "center",
                            "margin": "lg",
                            "size": "md",
                            "offsetTop": "xxl"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "符合此條件",
                                "text": "第三順位"
                            }
                        }
                    ]
                }
            }
        ]
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
