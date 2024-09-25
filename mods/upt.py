# This file is placed in the Public Domain.


"uptime"


import time


from otp.command import Commands
from otp.persist import laps
from otp.runtime import STARTTIME


def upt(event):
    "show uptime"
    event.reply(laps(time.time()-STARTTIME))


Commands.add(upt)
