from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    def __init__(self, *args) -> None:
        if self.__class__.__name__ == "Messenger":
            raise NotImplementedError("Messengerクラスを継承してください。")
        elif (not self.__class__.__name__ == "Sender") and (not self.__class__.__name__ == "Receiver"):
            raise TypeError("継承するクラスの名前はReceiverかSenderである必要があります。")

        self.args = args

    @abstractmethod
    def read(self, **arg) -> bytes:
        pass

    def read_str(self, **arg) -> str:
        """read()の戻り値をUTF-8の文字列に変換して返します。"""
        return self.read(**arg).decode("utf-8")

    @abstractmethod
    def write(self, contents: bytes, **arg) -> None:
        pass

    def write_str(self, contents: str, **arg) -> None:
        """write()の引数をUTF-8のバイト列に変換して渡します。"""
        self.write(contents.encode("utf-8"), **arg)

    @abstractmethod
    def communicate(self) -> None:
        """karadaとの通信を開始します"""
        pass
