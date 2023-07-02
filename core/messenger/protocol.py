from typing import Any, List, Dict
from dataclasses import dataclass


@dataclass
class SayArgs:
    message: List[str]


@dataclass
class Say:
    command: str
    args: SayArgs


def generate_say_command(args: SayArgs) -> Say:
    return Say(command='Say', args=args)


@dataclass
class SleepArgs:
    time: float


@dataclass
class Sleep:
    command: str
    args: SleepArgs


def generate_sleep_command(args: SleepArgs) -> Sleep:
    return Sleep(command='Sleep', args=args)


@dataclass
class LoadCharacterArgs:
    name: str
    path: str
    description: str
    license: str


@dataclass
class LoadCharacter:
    command: str
    args: LoadCharacterArgs


def generate_loadcharacter_command(args: LoadCharacterArgs) -> LoadCharacter:
    return LoadCharacter(command='LoadCharacter', args=args)


@dataclass
class TestArgs:
    message: str
    time: float
    number: int
    boolean: bool
    list: List[str]
    nest: Dict[str, Any]


@dataclass
class Test:
    command: str
    args: TestArgs


def generate_test_command(args: TestArgs) -> Test:
    return Test(command='Test', args=args)
