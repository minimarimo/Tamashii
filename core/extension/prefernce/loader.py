import os
import inspect
import importlib.util
from types import ModuleType

from core.extension.prefernce.data import HookData, SenderData, ReceiverData


def load_library(path_name: str, location: str) -> ModuleType:
    """
    指定されたlocationから指定されたpath_nameでモジュールを読み込みます。

    :param path_name: spec_from_file_locationの第一引数(name)に渡す名前
    :param location: spec_from_file_locationの第二引数(location)に渡すファイルの場所
    :return: 呼び出し可能なモジュール
    """
    spec = importlib.util.spec_from_file_location(path_name, location)
    imported_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(imported_module)

    return imported_module


def load_hook(hook_preference: HookData):
    """
    extension.scriptから拡張機能として定義されたスクリプトを読み、
    DesktopMascotController._script_functionに格納する
    """

    def load_and_get_static_method(path_name: str, location: str, class_name: str) -> dict[str, staticmethod]:
        imported_module = load_library(path_name, location)
        try:
            cls = getattr(imported_module, class_name)
        except AttributeError as e:
            print(e)
            return {}
        method = {}
        for path_name, function in inspect.getmembers(cls):
            if isinstance(cls.__dict__.get(path_name), staticmethod):
                method[path_name] = function
        return method

    for path in hook_preference.path:
        module = load_and_get_static_method(f"extension.script.{os.path.splitext(os.path.basename(path))[0]}",
                                            f"./extension/hook/{path}",
                                            "Extension")
        script_function: dict[str, list[staticmethod]] = {}
        for name, fn in module.items():
            if name not in script_function.keys():
                script_function[name] = []
            script_function[name].append(fn)
        return script_function


def load_sender(preference: SenderData):
    return load_library(f"extension.core.sender",
                        f"./extension/core/messenger/{preference.path}").Sender(**preference.args)


def load_receiver(preference: ReceiverData):
    return load_library(f"extension.core.receiver",
                        f"./extension/core/messenger/{preference.path}").Receiver(**preference.args)
