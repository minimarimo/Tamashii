from dataclasses import dataclass
from typing import Dict, List


@dataclass
class SenderData:
    """Config.core.messenger.sender: karadaへの送信に使用するための設定"""
    path: str
    args: Dict


@dataclass
class ReceiverData:
    """Config.core.messenger.receiver: karadaからの受信に使用するための設定"""
    path: str
    args: Dict


@dataclass
class MessengerData:
    """Config.core.messenger: karadaとの通信に使用するための設定"""
    sender: SenderData
    receiver: ReceiverData


@dataclass
class CoreData:
    """Config.core: coreで直接動作する機能の設定がある"""
    messenger: MessengerData
    ui: str


@dataclass
class ModelData:
    """Config.extension.model: モデルの設定がある"""
    name: str
    description: str
    path: str


@dataclass
class ScenarioData:
    """Config.extension.scenario: シナリオの設定がある"""
    name: str
    description: str
    path: str


@dataclass
class HookData:
    """Config.extension.hook: tamashiiの動作を拡張する"""
    is_enabled: bool
    path: List[str]


@dataclass
class ExtensionData:
    """Config.extension: coreを除く拡張機能の設定がある"""
    model: List[ModelData]
    scenario: List[ScenarioData]
    hook: HookData


@dataclass
class PreferenceData:
    """設定ファイルそのもの"""
    author: str
    core: CoreData
    extension: ExtensionData
