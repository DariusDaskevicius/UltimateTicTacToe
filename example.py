import sys
from time import sleep


class ActionTemplate:
    all_actions = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if not hasattr(cls, "func"):
            raise ValueError(f"Class does not implement the func API: {cls.__name__}")

        cls.all_actions[cls.__name__] = cls


class Wait(ActionTemplate):
    @classmethod
    def func(cls, duration: str):
        """Execution of teststeps is paused for the defined duration"""
        duration = float(duration)
        if duration <= 0:
            raise ValueError(
                f"Parameter 'duration' has to be greater than 0: {duration!r}"
            )

        print(f"sleeping for: {duration}s")
        sleep(duration)


class Beep(ActionTemplate):
    @classmethod
    def func(cls, duration: str = "50", frequency: str = "500"):
        """Make a beep sound for a given duration at a given frequency"""
        duration = int(duration)
        frequency = int(frequency)

        if not 0 < duration <= sys.maxsize:
            raise Exception(
                f"Parameter 'duration' has to be in the range of [0, {sys.maxsize}]: {duration}"
            )

        if not 37 <= frequency <= 32767:
            raise Exception(
                f"Parameter 'frequency' has to be in the range [37, 32767]: {frequency}"
            )

        beep(frequency, duration)


class BeepBetter(ActionTemplate):
    @classmethod
    def func(cls):
        print("BeepBetter")


print(ActionTemplate.all_actions)

try:

    ActionTemplate.all_actions["Wait"].func(duration="1")

    ActionTemplate.all_actions["BeepBetter"].func()
except:
    print("Error while running action")
