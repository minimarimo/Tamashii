from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class PreferenceData:
    default_speak_interval: int


@dataclass
class MessageData:
    OnFirstLoad: List[List[str]]
    OnLoad: List[List[str]]
    OnRandom: List[List[str]]


@dataclass
class LoadedScenarioData:
    """シナリオの設定がある"""
    # scenario: ScenarioData
    Preference: PreferenceData
    Dictionary: Dict[str, List[str]]
    Message: MessageData
