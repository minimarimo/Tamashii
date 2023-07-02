from dataclasses import dataclass
from typing import Any, List, Dict


@dataclass
class Nest:
    key: str
    message: str
    time: float
    number: int
    boolean: bool
    hogeofoajweiojfoiaewiofeioawfoaw: List[str]


@dataclass
class SayArgs:
    message: List[str]


@dataclass
class Say:
    command: str
    args: SayArgs


@dataclass
class SleepArgs:
    time: float


@dataclass
class Sleep:
    command: str
    args: SleepArgs


@dataclass
class TestArgs:
    message: str
    time: float
    number: int
    boolean: bool
    list: List[str]
    nest: Nest


@dataclass
class Test:
    command: str
    args: TestArgs


def say(args: SayArgs) -> Say:
    return Say(command='say', args=args)


def sleep(args: SleepArgs) -> Sleep:
    return Sleep(command='sleep', args=args)


def test(args: TestArgs) -> Test:
    return Test(command='test', args=args)
