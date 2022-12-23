import pandas as pd
from utils import send_text_message

#list(set(df['MarketName']))


class note(object):
    def __init__(self):
        note = {
            "uid" : [],  #user
            "character" : [],  #the one who do the things
            "type": [],  #good or bad
            "context": [] #what happen
        }
        self.note = pd.DataFrame(note)
        self.note.columns = ["uid", "character", "type", "context"]  #自訂欄位名稱
    
    # to know who is in the note 
    def get_member(self, event):

        user = event.source.user_id
        list_tem = self.note[self.note["uid"]==user]
        members_list = list(set(list_tem['character']))

        return members_list

    def search_someone(self, event, character):
        things_list = ""
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)&(self.note["character"]==character)]
        list_tem.reset_index(inplace=True,drop=True) #chceck user
        print("test")
        print("test")
        print("test")
        print(self.note)
        print("test")
        print(list_tem)
        for index in range(list_tem.shape[0]):
            things_list += (list_tem["type"][index] + "   " + list_tem["context"][index])
            if(index<list_tem.shape[0]-1): things_list += "\n"

        return things_list

    def search_sometype(self, event, type):
        things_list = ""
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)]
        list_tem.reset_index(inplace=True,drop=True) #chceck user
        if ((type =="仇") |(type =="恩")):  list_tem_type = list_tem[(list_tem["type"]==type)]
        list_tem_type.reset_index(inplace=True,drop=True) #chceck user
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print(self.note)
        print("test")
        print(list_tem)
        print("test")
        print(list_tem_type)
        print("test")
        if(list_tem_type.shape[0]!=0):
            for index in range(list_tem_type.shape[0]):
                things_list += (str(list_tem_type["character"][index]) + "   " + str(list_tem_type["context"][index]))
                if(index<list_tem_type.shape[0]-1):things_list += "\n"

        return things_list

    def search_someone_with_number(self, event, character, type):
        things_list = ""
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)&(self.note["character"]==character)&(self.note["type"]==type)]
        list_tem.reset_index(inplace=True,drop=True) #chceck user
        for index in range(list_tem.shape[0]):
            things_list += (str(index)+"   "+ str(list_tem["type"][index]) + "   " + str(list_tem["context"][index]))
            if(index<list_tem.shape[0]-1):things_list += "\n"

        return things_list

    def delete(self, event, character, number, type):
        things_list = ""
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)&(self.note["character"]==character)&(self.note["type"]==type)] #chceck user
        list_tem.reset_index(inplace=True,drop=True) 
        list_tem = list_tem.drop(int(number))
        list_tem.reset_index(inplace=True,drop=True)
        old_list = self.note[(self.note["uid"]!=user)|(self.note["character"]!=character)|(self.note["type"]!=type)] #chceck user
        self.note = pd.concat([old_list, list_tem])
        self.note.reset_index(inplace=True,drop=True)
        for index in range(list_tem.shape[0]):
            things_list += (str(index)+"   "+ list_tem["type"][index] + "   " + list_tem["context"][index])
            if(index<list_tem.shape[0]-1):things_list += "\n"

        return things_list

    def update(self, event, character, number, text, type):

        things_list = ""
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)&(self.note["character"]==character)&(self.note["type"]==type)] #chceck user
        list_tem.reset_index(inplace=True,drop=True) 
        print(list_tem)
        list_tem.loc[int(number), "context"] =  text
        old_list = self.note[(self.note["uid"]!=user) | (self.note["character"]!=character)|(self.note["type"]!=type)] 
        self.note = pd.concat([old_list, list_tem])
        self.note.reset_index(inplace=True,drop=True)
        print(list_tem)
        for index in range(list_tem.shape[0]):
            things_list += (str(index)+"   "+ list_tem["type"][index] + "   " + list_tem["context"][index])
            if(index<list_tem.shape[0]-1):things_list += "\n"

        return things_list

    def add_to_note(self, event, type, character):
        self.note = self.note.append({
            "uid" : event.source.user_id,  #user
            "character" : character,  #the one who do the things
            "type": type,  #good or bad
            "context": event.message.text #what happen
        },ignore_index=True
        )
        print(self.note)

    def someone_number_of_things(self, event, character, type):

        things_list = ""
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)&(self.note["character"]==character)&(self.note["type"]==type)] #chceck user

        return list_tem.shape[0]
    
    def name_valid(self, event, character):

        valid_name = False
        user = event.source.user_id
        list_tem = self.note[(self.note["uid"]==user)] #chceck user
        list_tem = list_tem["character"]
        print(list_tem)
        valid_name = character in list_tem.values

        return valid_name