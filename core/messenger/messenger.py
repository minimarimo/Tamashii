from core.messenger.sender import Sender
from core.messenger.receiver import Receiver
from core.extension.prefernce.data import MessengerData


class Messenger:
    def __init__(self, messenger: MessengerData):
        self.sender = Sender(messenger.sender)
        self.receiver = Receiver(messenger.receiver)
