# This file is placed in the Public Domain.


"uptime"


import time


from otp.client  import laps
from otp.runtime import STARTTIME


def upt(event):
    event.reply(laps(time.time()-STARTTIME))
