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
        setname(name)


def setname(name):
    "update config to a new name."
    setattr(Config, "name", name or Default.__module__.split(".", maxsplit=2)[-2])
    setattr(Config, "wdr", os.path.expanduser(f"~/.{name}"))
    setattr(Config, "pidfile", os.path.join(wdr, f"{name}.pid"))
    Workdir.wdr = Config.wdr


def __dir__():
    return (
        'Config',
        'setname'
    )
