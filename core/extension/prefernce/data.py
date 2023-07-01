from dataclasses import dataclass
from typing import get_type_hints, get_args, get_origin, Dict, List


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


def from_dict(data_class, data):
    if get_origin(data_class) is list:
        # It's a List type
        return [from_dict(get_args(data_class)[0], item) for item in data]
    elif get_origin(data_class) is dict:
        # It's a Dict type
        args = get_args(data_class)
        if args:  # if args is not empty, i.e., key and value types are specified
            key_type, value_type = args
            return {key_type(key): from_dict(value_type, value) for key, value in data.items()}
        else:  # if args is empty, i.e., key and value types are not specified
            return data
    elif get_origin(data_class) is None:
        # It's not a higher level type like List or Dict
        if data_class in (int, str, bool):  # add more basic types if needed
            return data
        else:
            # It's a dataclass
            return data_class(**{key: from_dict(value, data[key]) for key, value in get_type_hints(data_class).items() if key in data})
