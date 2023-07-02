from threading import Thread

from core.extension.prefernce.data import PreferenceData
from core.extension.scenario.data import LoadedScenarioData
from core.extension.prefernce.loader import load_hook
from core.extension.scenario.loader import load_scenario
from core.messenger.messenger import Messenger
from core.messenger.protocol import *


class DesktopMascotController:
    """
    デスクトップマスコットの全て。ここで何もかもコントロールする
    """
    hooks: dict[str, list[staticmethod]]
    """拡張機能で実装された関数が格納されています"""
    scenario: LoadedScenarioData
    """キャラの発言タイミングとその内容が格納されています"""

    def __init__(self, preference: PreferenceData):
        DesktopMascotController.hooks = load_hook(preference.extension.hook)
        self._preference = preference
        """拡張のために実装された関数を格納する"""
        self._messenger = Messenger(preference.core.messenger)
        # self._ui = load_ui(preference.core.ui)
        # self._model = load_model(preference.extension.model)
        DesktopMascotController.scenario = load_scenario(preference.extension.scenario)

    @classmethod
    def get_scenario(cls) -> LoadedScenarioData:
        """
        キャラの発言タイミングとその内容を返します
        """
        return cls.scenario

    def _run_sender(self):
        """
        karadaにメッセージを送信する
        """
        sender = self._messenger.sender
        sender.connect()
        while not sender.is_available():
            # 本来ならここで何の行動をするか判断する実装が入る
            # 今は開発中なのでSayコマンドのみの実装
            message = input("喋る内容を入力してください:")
            print("sender message: " + message)
            sender.write_str(say(SayArgs([message])))
            response = sender.read_str()
            print("sender response: " + response)

    def _run_receiver(self):
        """
        karadaから送られてきたメッセージを受信する
        """
        receiver = self._messenger.receiver
        receiver.connect()
        while not receiver.is_available():
            message = "Hello! from receiver!"
            print("receiver message: " + message)
            receiver.write_str(message)
            response = receiver.read_str()
            print("receiver response: " + response)

    def start(self):
        """
        デスクトップマスコットの起動
        """
        Thread(target=self._run_sender).start()
        # Thread(target=self._run_receiver).start()
