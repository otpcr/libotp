# This file is placed in the Public Domain.


"uptime"


import time


from otp.runtime import STARTTIME
from otp.utils   import laps


def upt(event):
    "show uptime"
    event.reply(laps(time.time()-STARTTIME))
