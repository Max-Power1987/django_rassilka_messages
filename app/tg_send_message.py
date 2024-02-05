from socket import if_nameindex
from Config import API_hash, API_id, Phone_number
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest, GetContactIDsRequest
from telethon.tl.types import InputPhoneContact
import os




class Tg_sender:
    def __init__(self, **kwargs):
        self.api_id = API_id
        self.api_hash = API_hash
        self.client = TelegramClient('sender_messagi', api_id=self.api_id, api_hash=self.api_hash).start(Phone_number)
        

    def send_to_user(self, user, text):
        with self.client as client:
            entity = client.get_entity(user)
            client.send_message(entity = entity, message = text)
            client(DeleteContactsRequest(id = [entity.id]))
            dialogs = client.get_dialogs()
            client.delete_dialog(dialogs[0])
            
    def send_phone(self, phone, text):
        with self.client as client:
            re = client(ImportContactsRequest(
            contacts=[InputPhoneContact(
            client_id = 1,
            phone= phone,
            first_name= phone,
            last_name= phone
            )]
            ))
            entity = client.get_entity(phone)
            client.send_message(entity = entity, message = text)
            client(DeleteContactsRequest(id = [entity.phone]))
            dialogs = client.get_dialogs()
            client.delete_dialog(dialogs[0])

def main():
    
    with open('phone.txt', 'r') as f:
        text = f.readline
    print(text)
if __name__ == '__main__':
    main()
