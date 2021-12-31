from transitions.extensions import GraphMachine

from utils import push_text_message, send_flex_message, send_latest_news, send_text_message, flex_message_contents


def create_machine():
    machine = TocMachine(
        states=["user", "menu", "apply_document",
                "school_transfer", "grade_report", "english_report", "chinese_report", "both_report",
                "student_status", "chinese_graduate_certificate", "change_profile", "reissue_student_id_card",
                "register_question", "in_school_district", "not_qualified", "graduate_in_taipei", "graduate_outside",
                "additional_quota", "change_distribution", "first_pick", "determine_second_or_third", "second_pick", "third_pick",
                "latest_news"],
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
                "dest": "latest_news",
                "conditions": "is_going_to_latest_news",
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
            {
                "trigger": "advance",
                "source": "apply_document",
                "dest": "student_status",
                "conditions": "is_going_to_student_status",
            },
            {
                "trigger": "advance",
                "source": "apply_document",
                "dest": "chinese_graduate_certificate",
                "conditions": "is_going_to_chinese_graduate_certificate",
            },
            {
                "trigger": "advance",
                "source": "apply_document",
                "dest": "change_profile",
                "conditions": "is_going_to_change_profile",
            },
            {
                "trigger": "advance",
                "source": "apply_document",
                "dest": "reissue_student_id_card",
                "conditions": "is_going_to_reissue_student_id_card",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "register_question",
                "conditions": "is_going_to_register_question",
            },
            {
                "trigger": "advance",
                "source": "register_question",
                "dest": "in_school_district",
                "conditions": "is_going_to_in_school_district",
            },
            {
                "trigger": "advance",
                "source": "register_question",
                "dest": "not_qualified",
                "conditions": "is_going_to_not_qualified",
            },
            {
                "trigger": "advance",
                "source": "in_school_district",
                "dest": "graduate_in_taipei",
                "conditions": "is_going_to_graduate_in_taipei",
            },
            {
                "trigger": "advance",
                "source": "in_school_district",
                "dest": "graduate_outside",
                "conditions": "is_going_to_graduate_outside",
            },
            {
                "trigger": "advance",
                "source": "graduate_outside",
                "dest": "additional_quota",
                "conditions": "is_going_to_additional_quota",
            },
            {
                "trigger": "advance",
                "source": "graduate_outside",
                "dest": "change_distribution",
                "conditions": "is_going_to_change_distribution",
            },
            {
                "trigger": "advance",
                "source": "graduate_in_taipei",
                "dest": "first_pick",
                "conditions": "is_going_to_first_pick",
            },
            {
                "trigger": "advance",
                "source": "graduate_in_taipei",
                "dest": "determine_second_or_third",
                "conditions": "is_going_to_determine_second_or_third",
            },
            {
                "trigger": "advance",
                "source": "determine_second_or_third",
                "dest": "second_pick",
                "conditions": "is_going_to_second_pick",
            },
            {
                "trigger": "advance",
                "source": "determine_second_or_third",
                "dest": "third_pick",
                "conditions": "is_going_to_third_pick",
            },
            {
                "trigger": "go_back",
                "source":
                ["school_transfer", "english_report",
                 "chinese_report", "both_report", "student_status", "chinese_graduate_certificate", "change_profile",
                 "reissue_student_id_card",
                 "not_qualified", "additional_quota", "change_distribution",
                 "first_pick", "second_pick", "third_pick", "latest_news"],
                "dest": "menu"
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine


class TocMachine(GraphMachine):

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

    def is_going_to_student_status(self, event):
        text = event.message.text
        return text == "在學證明書"

    def is_going_to_chinese_graduate_certificate(self, event):
        text = event.message.text
        return text == "中文畢業證明書"

    def is_going_to_change_profile(self, event):
        text = event.message.text
        return text == "個資異動"

    def is_going_to_reissue_student_id_card(self, event):
        text = event.message.text
        return text == "補辦數位學生證"

    def is_going_to_register_question(self, event):
        text = event.message.text
        return text == "設籍問題"

    def is_going_to_in_school_district(self, event):
        text = event.message.text
        return text == "是"

    def is_going_to_not_qualified(self, event):
        text = event.message.text
        return text == "否"

    def is_going_to_graduate_in_taipei(self, event):
        text = event.message.text
        return text == "是"

    def is_going_to_graduate_outside(self, event):
        text = event.message.text
        return text == "否"

    def is_going_to_additional_quota(self, event):
        text = event.message.text
        return text == "是"

    def is_going_to_change_distribution(self, event):
        text = event.message.text
        return text == "否"

    def is_going_to_first_pick(self, event):
        text = event.message.text
        return text == "是"

    def is_going_to_determine_second_or_third(self, event):
        text = event.message.text
        return text == "否"

    def is_going_to_second_pick(self, event):
        text = event.message.text
        return text == "第二順位"

    def is_going_to_third_pick(self, event):
        text = event.message.text
        return text == "第三順位"

    def is_going_to_latest_news(self, event):
        text = event.message.text
        return text == "查看教育局最新公告"

    def on_enter_menu(self, event):
        send_flex_message(event.source.user_id,
                          flex_message_contents["menu"])

    def on_enter_apply_document(self, event):
        send_flex_message(event.source.user_id,
                          flex_message_contents["apply_document_menu"])

    def on_enter_school_transfer(self, event):
        step = ("以下為申請 學生轉出 的流程： \n\n"
                "1. 至註冊組填寫「填寫異動申請書」\n"
                "2. 攜帶 2 吋相片三張、戶口名簿正影本、學生證、父母雙方監護人身分證及印章、其他相關資料 \n\n"
                "轉至其他學區公立國中 ：戶籍異動至該校學區 \n"
                "轉出國外 ：繳交護照正、影本 \n"
                "轉到私立學校 ：繳交繳費收據正、影本\n\n"
                "備註： 若成績系統正常，可現場領取。"
                )
        send_text_message(event.reply_token, step)

        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_grade_report(self, event):
        send_flex_message(event.source.user_id,
                          flex_message_contents["grade_report"])

    def on_enter_english_report(self, event):
        step = ("以下為申請 英文成績證明書 的流程：\n\n"
                "1. 至註冊組填寫「英文成績證明申請登記簿」\n\n"
                "2. 攜帶 2 吋相片 ( 張數同申請成績單份數 ) 、護照。\n\n"
                "3. 本人親辦：學生證（在學）或身分證（已畢業）\n\n"
                "4. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n"
                "備註： 約需 3 個工作天。"
                )
        send_text_message(event.reply_token, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_chinese_report(self, event):
        step = ("以下為申請 中文成績證明書 的流程：\n\n"
                "1. 至註冊組填寫「中文成績證明書申請登記簿」\n\n"
                "2. 本人親辦：學生證（在學）或身分證（已畢業）\n\n"
                "3. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n"
                "4. 中文成績證明書 :學期成績證明書(百分制)\n\n"
                "備註： 約需 3 個工作天。"
                )
        send_text_message(event.reply_token, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_both_report(self, event):
        english = ("以下為申請 英文成績證明書 的流程：\n\n"
                   "1. 至註冊組填寫「英文成績證明申請登記簿」\n\n"
                   "2. 攜帶 2 吋相片 ( 張數同申請成績單份數 ) 、護照。\n\n"
                   "3. 本人親辦：學生證（在學）或身分證（已畢業）\n\n"
                   "4. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n"
                   "備註： 約需 3 個工作天。"
                   )
        chinese = ("以下為申請 中文成績證明書 的流程：\n\n"
                   "1. 至註冊組填寫「中文成績證明書申請登記簿」\n\n"
                   "2. 本人親辦：學生證（在學）或身分證（已畢業）\n\n"
                   "3. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n"
                   "4. 中文成績證明書 :學期成績證明書(百分制)\n\n"
                   "備註： 約需 3 個工作天。\n\n"
                   )
        push_text_message(event.source.user_id, chinese +
                          "----------------------------------------------------\n"+english)

        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_student_status(self, event):
        step = ("以下為申請 在學證明書 的流程：\n\n"
                "1. 至註冊組填寫「在學證明書申請登記簿」。\n\n"
                "2. 本人親辦：請攜帶兩吋照片(張數同申請份數)\n\n"
                "3. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n"

                "備註： 約需 3 個工作天。"
                )
        push_text_message(event.source.user_id, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_chinese_graduate_certificate(self, event):
        step = ("以下為申請 中文畢業證明申請書 的流程：\n\n"
                "1. 至註冊組填寫「中文畢業證明申請書」。\n"
                "未滿 20 歲另需出具家長簽章之切結書。\n\n"
                "2.2 吋相片一張\n\n"
                "3. 本人親辦：學生證（在學）或身分證（已畢業）\n\n"
                "4. 親友代辦：代辦人身分證及學生身分證或戶口名簿\n\n"
                "5.畢業證書遺失須重新補發中文畢業證明書。\n\n"
                "備註： 約需 3 個工作天。"
                )
        push_text_message(event.source.user_id, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_change_profile(self, event):
        step = ("以下為申請 個資異動 的流程：\n\n"
                "攜帶三個月內戶籍謄本正本至註冊組辦理。"
                )
        push_text_message(event.source.user_id, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_reissue_student_id_card(self, event):
        step = ("以下為申請 補辦數位學生證 的流程：\n\n"
                "1. 至註冊組填寫「學生證補發申請單」，並經家長、導師簽章。\n\n"
                "2. 到總務處出納組繳交製卡費 11 3元(二代卡)，再將申請單繳回註冊組。\n\n"
                "備註： 學生證由教育局資訊室製發，完成後由學校派員領回，再通知學生領取，約 14 個工作天。"
                )
        push_text_message(event.source.user_id, step)
        msg = """感謝您使用本服務，即將回到主選單！"""
        push_text_message(event.source.user_id, msg)
        self.go_back(event)

    def on_enter_register_question(self, event):
        push_text_message(event.source.user_id, "以下為符合敦化國中學區的里別：")
        # 列出學區
        send_flex_message(event.source.user_id,
                          flex_message_contents["register_question"])
        send_flex_message(event.source.user_id,
                          flex_message_contents["in_area_or_not"])

    def on_enter_in_school_district(self, event):
        send_flex_message(event.source.user_id,
                          flex_message_contents["in_taipei_or_not"])

    def on_enter_not_qualified(self, event):
        push_text_message(event.source.user_id, "您不符合入學資格！")
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)

    def on_enter_graduate_in_taipei(self, event):
        send_flex_message(event.source.user_id,
                          flex_message_contents["graduate_in_taipei"])
        send_flex_message(event.source.user_id,
                          flex_message_contents["have_house_or_not"])

    def on_enter_graduate_outside(self, event):
        send_flex_message(event.source.user_id,
                          flex_message_contents["graduate_in_taipei"])
        send_flex_message(event.source.user_id,
                          flex_message_contents["have_house_or_not"])

    def on_enter_additional_quota(self, event):
        push_text_message(event.source.user_id, "您將以 外加名額 的分發方式入學！")
        push_text_message(event.source.user_id,
                          ("請在教育局規定的時間內(約七月份)至註冊組進行審查\n"
                           "並且備妥資料：\n\n"
                           "1. 有權狀(所有權人為直系二等親)：\n"
                           "  1)七月份戶籍謄本(全戶於前一年12月31日前設籍)\n"
                           "  2)當年1-7月任一月份之水費或電費收據正影本\n"
                           "  3)權狀正影本(於前一年12月31日前登記)\n"
                           "  4)國民小學畢業證書\n"
                           "  5)家長印章\n\n"

                           "2. 租屋：\n"
                           "  1)七月份戶籍謄本(全戶須設籍6年以上)\n"
                           "  2)當年1-7月任一月份之水費或電費收據正影本\n"
                           "  3)經公證之房屋租賃證明(6年以上)\n"
                           "  4)國民小學畢業證書\n"
                           "  5)家長印章\n"
                           ))
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)

    def on_enter_change_distribution(self, event):
        push_text_message(event.source.user_id,
                          ("您不符合入學資格，將改分發入學。\n"
                           "額滿學校會由教育部指定改分發學校，今年的選擇為：\n"
                           "長安、五常、民生國中\n"
                           "可自行選擇要改分發至哪所學校。"))
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)

    def on_enter_first_pick(self, event):
        push_text_message(event.source.user_id, "您的分發結果為 第一順位 ！")
        push_text_message(event.source.user_id,
                          ("請在教育局規定的時間內(約五月份)至註冊組進行複審\n"
                           "並且備妥資料：\n\n"
                           "1. 有權狀(所有權人為直系二等親)：\n"
                           "  1)五月份戶籍謄本(全戶於前一年12月31日前設籍)\n"
                           "  2)當年1-5月任一月份之水費或電費收據正影本\n"
                           "  3)權狀正影本(於前一年12月31日前登記)\n\n"

                           "2. 租屋：\n"
                           "  1)五月份戶籍謄本(全戶須設籍6年以上)\n"
                           "  2)當年1-5月任一月份之水費或電費收據正影本\n"
                           "  3)經公證之房屋租賃證明(6年以上)\n"
                           ))
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)

    def on_enter_determine_second_or_third(self, event):
        push_text_message(event.source.user_id, "請問您符合以下何種情況？")
        send_flex_message(event.source.user_id,
                          flex_message_contents["determine_second_or_third"])

    def on_enter_second_pick(self, event):
        push_text_message(event.source.user_id, "您的分發結果為 第二順位 ！")
        push_text_message(event.source.user_id,
                          ("若 第一順位 之學生分發完後仍有缺額，\n"
                           "則由 第二順位 之學生 依照 「學生設籍時間」 順序排序\n\n"
                           "若名額已滿，請家長上網填寫改分發志願至鄰近國中就讀。\n"
                           "今年改分發學校為：\n"
                           "長安、五常、民生國中"))
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)

    def on_enter_third_pick(self, event):
        push_text_message(event.source.user_id, "您的分發結果為 第三順位 ！")
        push_text_message(event.source.user_id,
                          ("若 第一順位及第二順位 之學生分發完後仍有缺額，\n"
                           "則由 第三順位 之學生 依照 「學生設籍時間」 順序排序\n\n"
                           "若名額已滿，請家長上網填寫改分發志願至鄰近國中就讀。\n"
                           "今年改分發學校為：\n"
                           "長安、五常、民生國中"))
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)

    def on_enter_latest_news(self, event):
        send_latest_news(event.source.user_id)
        push_text_message(event.source.user_id, "感謝您使用本服務，即將回到主選單！")
        self.go_back(event)
