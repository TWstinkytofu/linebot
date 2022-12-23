#todo :modify the format(type menu to back to menu) , things state has error
from transitions.extensions import GraphMachine

from utils import *
from note  import *
from function import *

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.note = note() 
        self.machine = GraphMachine(model=self, **machine_configs)
        self.type_buffer  = "" #store "恩" or "仇"
        self.name_buffer = "" #store the name of the one do this thing
        self.access_type_buffer = "" #store CRUD
        self.number_buffer = 0 #store what thing user want to change
        self.list_number_buffer = 0 #stroe how many thing responded to the name
        self.reply_buffer = "" # store what to show
        self.state_buffer = "" #stroe the state before a error
        self.error_bit = False
        self.goback = False

    def is_going_to_name(self, event):
        text = event.message.text
        type_valid = ("功" in text)|("仇" in text)
        operation_valid = ("新增" in text)|("刪除" in text)|("修改" in text)
        search_someone = ("翻本" in text) & ("人" in text)
        return (type_valid&operation_valid)|search_someone
    
    def is_going_to_things(self, event):
        text = event.message.text
        return (("翻本" in text)& (("恩"in text) or ("仇"in text)))
    
    def is_going_to_Delete(self, event):
        text = event.message.text
        valid_number = False
        if(text.isdigit()):
            print(self.list_number_buffer)
            if(int(text)< self.list_number_buffer):
                valid_number = True
        if ((not valid_number)&(self.access_type_buffer == "D")): 
            self.reply_buffer = "請填入列表範圍內的阿拉伯數字，可輸入 返回 <數字>重新選擇໒(＾ᴥ＾)७"
            self.state_buffer = "D"
        return (self.access_type_buffer == "D")&valid_number

    def is_going_to_Update_choose(self, event):
        text = event.message.text
        valid_number = False
        if(text.isdigit()):
            if(int(text)< self.list_number_buffer):
                valid_number = True
        if ((not valid_number)&(self.access_type_buffer == "U")): 
            self.reply_buffer = "請填入列表範圍內的阿拉伯數字，可輸入 返回 <數字>重新選擇໒(＾ᴥ＾)७"
            self.state_buffer = "U"
        return (self.access_type_buffer == "U")&valid_number

    def is_going_to_Read(self, event):
        text = event.message.text
        return (self.access_type_buffer == "R")

    def is_going_to_list(self, event):
        text = event.message.text
        valid_name = self.note.name_valid(event, text)
        valid = ((self.access_type_buffer == "U")|(self.access_type_buffer == "D"))&valid_name
        if(not valid): 
            self.reply_buffer = "該名字未出現過，無法刪除或修改，可輸入 返回 <名字>重新選擇໒(＾ᴥ＾)७"
            self.state_buffer = "L"
        return valid

    def is_going_to_Create_things(self, event):
        return (self.access_type_buffer == "C")

    def go_back_list(self, event):
        text = event.message.text
        text_list = ""
        text_list = text.split(' ')
        valid = False
        valid_name = False
        if(len(text_list)!=1):
            valid_name = (self.note.name_valid(event, text_list[1]))
            valid = (text_list[0]=="返回")&valid_name
        if((not valid_name)&(self.state_buffer == "L")): 
            self.reply_buffer = "該名字未出現過，無法刪除或修改υ´• ﻌ •`υ"
            self.state_buffer = "L"
        go = (self.state_buffer == "L")&valid
        if(go) : self.goback = True

        return go

    def go_back_Update_choose(self, event):
        text = event.message.text
        text_list = ""
        text_list = text.split(' ')
        valid = False
        valid_number = False
        if(len(text_list)>1):
            print((text_list))
            print("pass len")
            print(text[1])
            if(text_list[1].isdigit()):
                print("pass digit")
                if(int(text_list[1])< self.list_number_buffer):
                    print("pass number")
                    valid_number = True
        if ((not valid_number)&(self.state_buffer == "U")): 
            self.reply_buffer = "請填入列表範圍內的阿拉伯數字υ´• ﻌ •`υ"
            self.state_buffer = "U"
        valid = valid_number&(text_list[0] == "返回")
        go = (self.state_buffer == "U")&valid
        if(go) : self.goback = True
        
        return go

    def go_back_Delete(self, event):
        text = event.message.text
        text_list = ""
        text_list = text.split(' ')
        valid = False
        valid_number = False
        if(len(text_list)>1):
            print((text_list))
            print("pass len")
            print(text[1])
            if(text_list[1].isdigit()):
                print("pass digit")
                if(int(text_list[1])< self.list_number_buffer):
                    print("pass number")
                    valid_number = True
        if ((not valid_number)&(self.state_buffer == "D")): 
            self.reply_buffer = "請填入列表範圍內的阿拉伯數字υ´• ﻌ •`υ"
            self.state_buffer = "D"
        valid = valid_number&(text_list[0] == "返回")
        go = (self.state_buffer == "D")&valid
        if(go) : self.goback = True
        
        return go

    def set_error(self):
        self.error_bit = True

#state user
    def on_enter_user(self, event):
        print("I'm entering ini_state")
        self.type_buffer  = ""
        self.name_buffer = ""

        reply_token = event.reply_token
        message = Carousel_Template()
        send_text_message(reply_token, message)

#menu 菜單        
    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        message = Carousel_Template()
        if(self.reply_buffer != ""):
            message = [TextSendMessage(text=self.reply_buffer) ,Carousel_Template()]
        elif(self.error_bit == True):
            message = [TextSendMessage(text="請輸入正確的格式૮ ・ﻌ・ა") ,Carousel_Template()]
        send_text_message_type2(reply_token, message)
        self.reply_buffer = ""
        self.error_bit = False

#input name
    def on_enter_name(self, event):

        print("I'm entering name")

        self.state_buffer = ""
        text = event.message.text
        if("仇" in text): self.type_buffer  = "仇"
        elif("功" in text): self.type_buffer  = "恩"
        else :self.type_buffer  = "翻"

        if("新增" in text): self.access_type_buffer  = "C"
        elif("修改" in text): self.access_type_buffer  = "U"
        elif("刪除" in text): self.access_type_buffer  = "D"
        else :self.access_type_buffer  = "R" #翻小本本

        print("I'm entering name")

        reply_token = event.reply_token
        send_text_message(reply_token, "拿出小本本૮ ˶′ﻌ ‵˶ ა \n請輸入名字")

#Create_things        
    def on_enter_Create_things(self, event):
        print("I'm entering Create_things")
        text = event.message.text

        reply_token = event.reply_token
        self.name_buffer = event.message.text
        send_text_message(reply_token, "拿起小筆筆໒( ̿･ ᴥ ̿･ )ʋ \n請輸入發生的事情")

#Delete
    def on_enter_Delete(self, event):
        print("I'm entering Delete")

        self.state_buffer = ""
        if(self.goback) : 
            text_list = event.message.text.split(' ')
            self.number_buffer = text_list[1]
        else : self.number_buffer = event.message.text
        self.goback = False
        message = self.note.delete(event, self.name_buffer, self.number_buffer, self.type_buffer)
        message = str(message)
        message += "已刪除૮ ˘ﻌ˘ ა"
        self.reply_buffer = message


#Update
    def on_enter_Update(self, event):
        print("I'm entering Update")

        reply_token = event.reply_token
        text = event.message.text
        message = self.note.update(event, self.name_buffer, self.number_buffer, text ,self.type_buffer)
        message = str(message)
        self.reply_buffer = message


#list
    def on_enter_list(self, event):
        print("I'm entering list")

        self.state_buffer = ""
        if(self.goback) : 
            text_list = event.message.text.split(' ')
            self.name_buffer = (text_list[1])
        else : self.name_buffer = event.message.text
        self.goback = False
        reply_token = event.reply_token
        message = self.note.search_someone_with_number(event, self.name_buffer, self.type_buffer)
        message = str(message)
        message += "\n輸入數字以選擇事件U ´ᴥ` U"
        self.list_number_buffer =self.note.someone_number_of_things(event, self.name_buffer, self.type_buffer)
        send_text_message(reply_token, message)

#thing with certain type
    def on_enter_things(self, event):
        print("I'm entering things")
        
        self.state_buffer = ""
        text = event.message.text
        if("仇" in text): self.type_buffer  = "仇"
        elif("恩" in text): self.type_buffer  = "恩"
        else :self.type_buffer  = "翻"

        reply_token = event.reply_token
        message = self.note.search_sometype(event, self.type_buffer)
        message = str(message)
        self.reply_buffer = message

# update thing input
    def on_enter_Update_choose(self, event):
        print("I'm entering Update_choose")
        
        self.state_buffer = ""
        if(self.goback) : 
            text_list = event.message.text.split(' ')
            self.number_buffer = int(text_list[1])
        else : self.number_buffer = event.message.text
        self.goback = False
        reply_token = event.reply_token
        message = "請輸入要修改的內容( ͡° ᴥ ͡° ʋ)"
        send_text_message(reply_token, message)

#Read 小本本的名字
    def on_enter_Read(self, event):
        print("I'm entering Read")

        reply_token = event.reply_token
        self.name_buffer = event.message.text
        message = self.note.search_someone(event, self.name_buffer)
        message = str(message)
        self.reply_buffer = message



#state7 記仇/功的事情
    def on_enter_Create(self, event):
        print("I'm entering Create")

        reply_token = event.reply_token
        print(self.type_buffer)
        self.note.add_to_note(event, self.type_buffer , self.name_buffer)
        if(self.type_buffer == "仇"): message = "這個仇，我記下了૮ ◣ ܫฺ ◢ა"
        else :message = "愛卿這功，朕銘記在心૮ ♡ﻌ♡ა"
        self.reply_buffer = message


