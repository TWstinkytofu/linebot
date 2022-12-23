#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img.freepik.com/free-photo/angry-golden-retriever-dog_1204-383.jpg?w=2000',
                    title='記仇',
                    text='舉世皆濁我獨清，眾人皆醉我獨醒',
                    actions=[
                        MessageTemplateAction(
                            label="再添一筆",
                            text="記仇_新增"
                        ),
                        MessageTemplateAction(
                            label='刪除舊帳',
                            text="記仇_刪除"
                        ),
                        MessageTemplateAction(
                            label='小做修改',
                            text="記仇_修改"
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/OhlQly4.jpg',
                    title='記功',
                    text='要謝得人太多了，那就謝天吧',
                    actions=[
                        MessageTemplateAction(
                            label="再添一筆",
                            text="記功_新增"
                        ),
                        MessageTemplateAction(
                            label='刪除舊帳',
                            text="記功_刪除"
                        ),
                        MessageTemplateAction(
                            label='小做修改',
                            text="記功_修改"
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/ej9vGxW.jpg',
                    title='翻小本本',
                    text='闔眼分是非對錯，可清明誤我',
                    actions=[
                        MessageTemplateAction(
                            label="有恩報恩",
                            text="翻本—計恩"
                        ),
                        MessageTemplateAction(
                            label='有仇報仇',
                            text="翻本—記仇"
                        ),
                        MessageTemplateAction(
                            label='對人不對事',
                            text="翻本—看人"
                        )
                    ]
                ),
            ]
        )
    )
    return message
