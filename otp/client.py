# This file is placed in the Public Domain.
# pylint: disable=R.W0105,W0212,W0718


"client"


import inspect
import os
import pathlib
import pwd
import sys
import termios
import time
import _thread


from .config  import Config
from .event   import parse
from .runtime import Reactor, later


class Broker:

    "Broker"

    objs = {}

    @staticmethod
    def add(obj, key):
        "add object."
        Broker.objs[key] = obj

    @staticmethod
    def all(kind=None):
        "return all objects."
        if kind is not None:
            for key in [x for x in Broker.objs if kind in x]:
                yield Broker.get(key)
        return Broker.objs.values()

    @staticmethod
    def get(orig):
        "return object by matching repr."
        return Broker.objs.get(orig)


class Client(Reactor):

    "Client"

    def __init__(self):
        Reactor.__init__(self)
        Broker.add(self, repr(self))
        self.register("command", command)

    def display(self, evt):
        "show results into a channel."
        for txt in evt.result:
            self.say(evt.channel, txt)

    def say(self, _channel, txt):
        "echo on verbose."
        self.raw(txt)

    def raw(self, txt):
        "print to screen."
        raise NotImplementedError


class Commands:

    "Commands"

    cmds     = {}
    modnames = {}

    @staticmethod
    def add(func):
        "add command."
        Commands.cmds[func.__name__] = func
        if func.__module__ != "__main__":
            Commands.modnames[func.__name__] = func.__module__


def command(bot, evt, txt=""):
    "check for and run a command."
    parse(evt, txt or evt.txt)
    func = Commands.cmds.get(evt.cmd, None)
    if func:
        func(evt)
        bot.display(evt)


def scan(mod):
    "Scan module for commands."
    for key, cmnd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith('cb'):
            continue
        names = cmnd.__code__.co_varnames
        if 'event' in names:
            Commands.add(cmnd)


"utilitites"


def banner(outer):
    "show banner."
    tme = time.ctime(time.time()).replace("  ", " ")
    outer(f"{Config.name.upper()} since {tme}")


def daemon(verbose=False):
    "switch to background."
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    os.nice(10)


def forever():
    "it doesn't stop, until ctrl-c"
    while True:
        try:
            time.sleep(1.0)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def laps(seconds, short=True):
    "show elapsed time."
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    yea = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    yeas = int(nsec/yea)
    nsec -= yeas*yea
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if yeas:
        txt += f"{yeas}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def modnames(*args):
    "return module names."
    res = []
    for arg in args:
        res.extend([x for x in dir(arg) if not x.startswith("__")])
    return sorted(res)


def pidfile(pid):
    "write the pid to a file."
    if os.path.exists(pid):
        os.unlink(pid)
    path = pathlib.Path(pid)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(pid, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


def privileges(username):
    "drop privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def scanner(modstr, *pkgs, disable=None):
    "scan modules for commands and classes"
    mods = []
    for mod in spl(modstr):
        if disable and mod in spl(disable):
            continue
        for pkg in pkgs:
            modi = getattr(pkg, mod, None)
            if not modi:
                continue
            scan(modi)
            mods.append(modi)
            break
    return mods


def spl(txt):
    "split comma separated string into a list."
    try:
        res = txt.split(',')
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def wrap(func, outer):
    "reset console."
    old3 = None
    try:
        old3 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        outer("")
    except Exception as ex:
        later(ex)
    finally:
        if old3:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old3)


def __dir__():
    return (
        'Broker',
        'Client',
        'Commands',
        'banner',
        'daemon',
        'forever',
        'laps',
        'modnames',
        'pidfile',
        'privileges',
        'scanner',
        'spl',
        'wrap',
        'wrapped'
    )
