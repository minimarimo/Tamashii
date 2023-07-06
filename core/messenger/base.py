import json
from dataclasses import asdict, is_dataclass
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    def __init__(self, *args) -> None:
        if self.__class__.__name__ == "Messenger":
            raise NotImplementedError("Messengerクラスを継承してください。")
        elif (not self.__class__.__name__ == "Sender") and (not self.__class__.__name__ == "Receiver"):
            raise TypeError("継承するクラスの名前はReceiverかSenderである必要があります。")

        self.args = args

    @abstractmethod
    def is_available(self) -> bool:
        """karadaとの通信が可能かどうかを返します。"""
        pass

    @abstractmethod
    def read(self, **kwargs) -> bytes:
        pass

    def read_str(self, **kwargs) -> str:
        """read()の戻り値をUTF-8の文字列に変換して返します。"""
        return self.read(**kwargs).decode("utf-8")

    @abstractmethod
    def write(self, contents: bytes, **kwargs) -> None:
        pass

    def write_str(self, contents, **kwargs) -> None:
        """write()の引数をUTF-8のバイト列に変換して渡します。"""
        def to_json(obj):
            if is_dataclass(obj):
                return json.dumps(asdict(obj))
            return json.dumps(obj)
        self.write((to_json(contents) + "\n").encode(), **kwargs)

    @abstractmethod
    def connect(self) -> None:
        """karadaとの通信を開始します"""
        pass
