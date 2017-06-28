
from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online_status = True
        self.chats = []
        self.current_status_message = None

spy=Spy('Bond','Mr',21,5.0)
user_spy_rating = 2.0

class ChatMessage:
    def __init__(self,message,length_chat,send_by_me):
        self.message=message
        self.time=datetime.now()
        self.length=length_chat
        self.sent_by_me=send_by_me

friends = []