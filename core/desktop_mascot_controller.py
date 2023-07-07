import random
from dataclasses import asdict
from threading import Thread
from typing import Optional, Type

from core.extension.prefernce.data import PreferenceData
from core.extension.scenario.data import LoadedScenarioData
from core.extension.prefernce.loader import load_hook
from core.extension.scenario.loader import load_scenario, parse_and_execute_scenario, ScenarioInstance
from core.messenger.messenger import Messenger
from core.messenger.protocol import *


class DesktopMascotController:
    """
    デスクトップマスコットの全て。ここで何もかもコントロールする
    """
    hooks: dict[str, list[staticmethod]]
    """拡張機能で実装された関数が格納されています"""

    def __init__(self, preference: PreferenceData):
        self._is_debug = True
        DesktopMascotController.hooks = load_hook(preference.extension.hook)
        self._preference = preference
        """拡張のために実装された関数を格納する"""
        self._messenger = Messenger(preference.core.messenger)
        # self._ui = load_ui(preference.core.ui)
        # self._model = load_model(preference.extension.model)
        self._scenario = load_scenario(preference.extension.scenario)
        self._scenario_instance = ScenarioInstance(preference)
        self._flags = {}
        """karadaから送られてきたフラグを格納する"""
        self.user_love_level = 50

        # FIXME: 本来なら今実行中のキャラの設定が入るのですが、今はデバッグなのでこうしてます
        self.my = self

    def _action(self):
        """
        キャラが行動し、その結果を返します。
        """
        action_result: list
        """キャラが行動を起こした結果です。"""
        # karadaが何か検知していないかやタイマーからなんか来てないかなどを確認する
        for flag in self._flags:
            if flag in self._scenario.Message:
                print(flag)
                # TODO: ここでフラグに応じた処理を実行し、送信するstrを返す

        # 何も起きていなければランダムにメッセージを送信する
        on_random = self._scenario.Message.OnRandom
        contents = on_random[random.randint(0, len(on_random) - 1)] if on_random else []
        action_result = parse_and_execute_scenario(contents, self, self._scenario_instance)

        return generate_say_command(SayArgs(message=action_result))

    def _run_sender(self):
        """
        karadaにメッセージを送信する
        """
        sender = self._messenger.sender
        sender.connect()
        # licenseはvrmから抽出するが、今は開発中なので固定値
        for model in self._preference.extension.model:
            sender.write_str(generate_loadcharacter_command(LoadCharacterArgs(**asdict(model), license="Dummy License")))
            sender.read_str()
            # とりあえず1キャラだけロード TODO: 複数キャラ
            break

        while sender.is_available():
            # 本来ならここで何の行動をするか判断する実装が入る
            # 今は開発中なのでSayコマンドのみの実装
            message = self._action()
            if not message:
                continue
            # message = input("喋る内容を入力してください:")
            # そう。ここが開発用のコードなので、SayArgsではなく適切なシナリオを読み込む関数に変わる
            print("送信: " + str(message))
            sender.write_str(message)
            response = sender.read_str()
            print("sender response: " + response)
            input("Press Enter to continue...")

    def _run_receiver(self):
        """
        karadaから送られてきたメッセージを受信する
        TODO: 未実装
        """
        receiver = self._messenger.receiver
        receiver.connect()
        while receiver.is_available():
            response = receiver.read_str()
            print("receiver response: " + response)
            message = "Hello! from receiver!"
            print("receiver message: " + message)
            receiver.write_str(message)

    def start(self):
        """
        デスクトップマスコットの起動
        """
        Thread(target=self._run_sender).start()
        # Thread(target=self._run_receiver).start()
