from core.messenger.sender import Sender
from core.messenger.receiver import Receiver
from core.extension.prefernce.data import MessengerData


class Messenger:
    def __init__(self, messenger: MessengerData):
        self._sender = Sender(messenger.sender)
        self._receiver = Receiver(messenger.receiver)

    def communicate(self):
        self._receiver.communicate()
        self._sender.communicate()
