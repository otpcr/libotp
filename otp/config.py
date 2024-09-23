# This file is placed in the Public Domain.
# pylint: disable=R0903


"configuration"


import os


from .object  import Default
from .persist import Workdir


class Config(Default):

    "Config"

    name = Default.__module__.split(".", maxsplit=2)[-2]
    wdr = os.path.expanduser(f"~/.{name}")
    pidfile = os.path.join(wdr, f"{name}.pid")

    def __init__(self, name=None):
        self.name = name or Config.name
        self.wdr = Config.wdr
        self.pidfile = Config.pidfile


Workdir.wdr = Config.wdr


def __dir__():
    return (
        'Config',
    )
