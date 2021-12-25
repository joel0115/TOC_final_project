from transitions.extensions import GraphMachine

from utils import push_text_message, send_flex_message, send_text_message


def create_machine():
    machine = TocMachine(
        states=["user", "menu", "apply_document",
                "school_transfer", "grade_report", "english_report", "chinese_report", "both_report"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "apply_document",
                "conditions": "is_going_to_apply_document",
            },

            {
                "trigger": "advance",
                "source": "apply_document",
                "dest": "school_transfer",
                "conditions": "is_going_to_school_transfer",
            },
            {
                "trigger": "advance",
                "source": "apply_document",
                "dest": "grade_report",
                "conditions": "is_going_to_grade_report",
            },
            {
                "trigger": "advance",
                "source": "grade_report",
                "dest": "english_report",
                "conditions": "is_going_to_english_report",
            },
            {
                "trigger": "advance",
                "source": "grade_report",
                "dest": "chinese_report",
                "conditions": "is_going_to_chinese_report",
            },
            {
                "trigger": "advance",
                "source": "grade_report",
                "dest": "both_report",
                "conditions": "is_going_to_both_report",
            },
            {"trigger": "go_back",
             "source":
             ["school_transfer", "english_report",
                 "chinese_report", "both_report"],
             "dest": "menu"
             },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine


class TocMachine(GraphMachine):
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

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "start" or text == "開始"

    def is_going_to_apply_document(self, event):
        text = event.message.text
        return text == "證明文件申請流程"

    def is_going_to_school_transfer(self, event):
        text = event.message.text
        return text == "學生轉出"

    def is_going_to_grade_report(self, event):
        text = event.message.text
        return text == "成績證明"

    def is_going_to_english_report(self, event):
        text = event.message.text
        return text == "英文成績證明書"

    def is_going_to_chinese_report(self, event):
        text = event.message.text
        return text == "中文成績證明書"

    def is_going_to_both_report(self, event):
        text = event.message.text
        return text == "以上皆是"

    def on_enter_menu(self, event):
        send_flex_message(event.source.user_id,
                          self.flex_message_contents["menu"])

    def on_enter_apply_document(self, event):
        send_flex_message(event.source.user_id,
                          self.flex_message_contents["apply_document_menu"])

    def on_enter_school_transfer(self, event):
        step = """以下為申請 學生轉出 的流程： \n
  1. 至註冊組填寫「填寫異動申請書」\n
  2. 攜帶 2 吋相片三張、戶口名簿正影本、學生證、父母雙方監護人身分證及印章、其他相關資料 \n\n
轉至其他學區公立國中 ：戶籍異動至該校學區 \n
轉出國外 ：繳交護照正、影本 \n
轉到私立學校 ：繳交繳費收據正、影本\n

備註： 若成績系統正常，可現場領取。
        """
        send_text_message(event.reply_token, step)

        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_grade_report(self, event):
        send_flex_message(event.source.user_id,
                          self.flex_message_contents["grade_report"])

    def on_enter_english_report(self, event):
        step = """以下為申請 英文成績證明書 的流程：\n
1. 至註冊組填寫「英文成績證明申請登記簿」\n\n
2. 攜帶 2 吋相片 ( 張數同申請成績單份數 ) 、護照。\n\n
3. 本人親辦：學生證（在學）或身分證（已畢業）\n\n
4. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n

備註： 約需 3 個工作天。
"""
        send_text_message(event.reply_token, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_chinese_report(self, event):
        step = """以下為申請 中文成績證明書 的流程：\n
1. 至註冊組填寫「中文成績證明書申請登記簿」\n\n
2. 本人親辦：學生證（在學）或身分證（已畢業）\n\n
3. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n
4. 中文成績證明書 :學期成績證明書(百分制)\n\n

備註： 約需 3 個工作天。
"""
        send_text_message(event.reply_token, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_both_report(self, event):
        english = """以下為申請 英文成績證明書 的流程：\n
1. 至註冊組填寫「英文成績證明申請登記簿」\n\n
2. 攜帶 2 吋相片 ( 張數同申請成績單份數 ) 、護照。\n\n
3. 本人親辦：學生證（在學）或身分證（已畢業）\n\n
4. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n

備註： 約需 3 個工作天。
"""
        chinese = """以下為申請 中文成績證明書 的流程：\n
1. 至註冊組填寫「中文成績證明書申請登記簿」\n\n
2. 本人親辦：學生證（在學）或身分證（已畢業）\n\n
3. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n
4. 中文成績證明書 :學期成績證明書(百分制)\n\n

備註： 約需 3 個工作天。\n\n
"""
        push_text_message(event.source.user_id, chinese +
                          "----------------------------------------------------\n"+english)

        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)
