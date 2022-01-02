# 註冊組疑難雜症小幫手

author F74082010 資訊系112級 陳昭穎

## 動機

我的家人在敦化國中的註冊組工作，不僅平常有許多與申請文件有關的問題，

每逢分發入學的時期就會有許多家長打電話來詢問入學資格相關問題。

而回答這些問題總是會浪費許多時間，造成其他種類的問題無法被快速回覆到。

因此我想藉由本次作業的機會來實作一個 Line 機器人，以便快速回覆家長們此類問題，節省大量時間！

## 功能簡介
1. 設籍問題

    可以查詢學生有沒有符合分發入學至敦化國中的資格，

    在經過ㄧ連串的問答後，可以知道自己分發入學的順位，

    並且如果需要複審的話，會告知複審所需準備的文件及審查的流程！

2. 證明文件申請流程

    若是學生有需要申請ㄧ些證明文件的話可以採用此功能，

    會根據學生選擇的文件類別，輸出對應的申請流程以及注意事項！


4. 查看教育局最新公告

    利用爬蟲的技巧，得到教育局中等教育科的國中新生入學的最新公告，

    讓家長可以不用在教育局的茫茫大海中找尋對新生有用的資訊！

## FSM 架構圖
以下為利用 GraphMachine 功能印出來的圖片
![fsm](https://user-images.githubusercontent.com/71745723/147857940-9dbbff96-89de-4677-a3a3-474c9808c0ee.png)

### State 說明
user: 最一開始加入 line bot 好友時進入的state，輸入 開始 或 start(大小寫沒關係) 即可進入到功能選單。

menu: 輸出功能選單，可以選擇查詢 設籍問題、證明文件申請流程 或是 查看教育局最新公告。

- apply_document: 輸出欲查詢的證明文件類別，供使用者選擇。
    - school_transfer: 輸出申請 學生轉出 的流程。

    - student_status: 輸出申請 在學證明書 的流程。

    - grade_report: 輸出申請 成績證明 的選項。
        - english_report: 輸出申請 英文成績證明 的流程。
        - chinese_report: 輸出申請 中文成績證明 的流程。
        - both_report: 輸出申請 中文及英文成績證明 的流程。
    - chinese_graduate_certificate: 輸出申請 中文畢業證明書 的流程。
    - change_profile: 輸出申請 個資異動 的流程
    - reissue_student_id_card: 輸出 補辦數位學生證 的流程。

- register_question: 輸出 符合敦化國中學區的里別，並且詢問是否設籍在其中的里。
    - in_school_district: 使用者有設籍在學區內，接著詢問是否在 台北市 畢業。
        - graduate_outside: 為外縣市畢業，接著詢問是否符合 自有房屋 或 租屋 的條件。
            - additional_quota: 符合條件，以 外加名額 方式入學，並且輸出審查方式。
            - change_distribution: 不符合條件，需要改分發，輸出改分發的學校選項。

        - graduate_in_taipei: 在台北市畢業，接著詢問是否符合 自有房屋 或 租屋 的條件。
            - first_pick: 符合條件，為 第一順位 的學生，輸出複審的時程和流程。
            - determine_second_or_third: 不符合條件，詢問 父母與學生的設籍狀況。
                - second_pick: 符合 父母與學生三人共同設籍，若為單親須與法定監護人設籍 的條件，因此為 第二順位，輸出分發的規則。
                - third_pick: 符合 父或母只有一位與學生共同設籍 的條件，因此為 第三順位，輸出分發的規則。 
    - not_qualified: 因為不設籍在學區內，輸出 不符合資格 的相關訊息。

- latest_news: 輸出 教育局中等教育科 的國中新生入學區最新的前五個公告 (利用爬蟲的方式取得)。
## DEMO

### 設籍問題

#### 第一順位

![Screenshot_2022-01-02-02-59-18-385_jp naver line android](https://user-images.githubusercontent.com/71745723/147874423-53909bb4-da59-4430-8dc5-b0377696d0c9.png)
---

#### 第二順位

![Screenshot_2022-01-02-19-34-18-726_jp naver line android](https://user-images.githubusercontent.com/71745723/147874521-d1ca6a0e-8b10-44bc-adf9-9dff23a493b4.png)
---

#### 第三順位

![Screenshot_2022-01-02-19-35-07-380_jp naver line android](https://user-images.githubusercontent.com/71745723/147874515-97c6d855-5f5d-4df7-a64a-ea4d7120370d.png)

---
#### 外加名額

![Screenshot_2022-01-02-19-45-51-860_jp naver line android](https://user-images.githubusercontent.com/71745723/147874785-a9923143-f228-4618-b672-53b07b099bc5.png)

---

#### 資格不符

![Screenshot_2022-01-02-19-45-16-614_jp naver line android](https://user-images.githubusercontent.com/71745723/147874779-a94648d0-fca7-4f88-ab46-299956a4b85a.png)

---

### 證明文件申請流程

#### 學生轉出

![Screenshot_2022-01-02-02-54-12-467_jp naver line android](https://user-images.githubusercontent.com/71745723/147874598-f24056db-bd1e-4ec3-ba25-08c89ef8ceb5.png)
---

#### 成績證明

![Screenshot_2021-12-26-17-44-52-633_jp naver line android](https://user-images.githubusercontent.com/71745723/147874631-58b05fa5-d2ce-4828-8937-b2348bca3a29.png)
---

#### 在學證明書

![Screenshot_2022-01-02-02-55-26-307_jp naver line android](https://user-images.githubusercontent.com/71745723/147874636-3913ce87-2b49-4615-a788-56e301afbb6a.png)
---

#### 中文畢業證明書

![Screenshot_2022-01-02-02-55-49-691_jp naver line android](https://user-images.githubusercontent.com/71745723/147874643-97b2c158-7a8d-4e1c-ba4e-1380c2383138.png)

---

#### 補辦數位學生證

![Screenshot_2022-01-02-02-56-14-160_jp naver line android](https://user-images.githubusercontent.com/71745723/147874648-a298a0c3-30fd-4d3a-91af-12dabcd18510.png)

---

#### 個資異動

![Screenshot_2022-01-02-02-56-32-700_jp naver line android](https://user-images.githubusercontent.com/71745723/147874655-da4bc51c-5d81-459c-a900-f54ce49ea840.png)

---

### 查看教育局最新公告
![Screenshot_2022-01-02-02-56-50-206_jp naver line android](https://user-images.githubusercontent.com/71745723/147874577-d5eaac2f-d861-46f2-9bec-ba4c3b3e7c79.png)
