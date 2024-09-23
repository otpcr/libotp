# This file is placed in the Public Domain.
# pylint: disable=R


"event"


from .object import Default


class Event(Default):

    "Event"

    def __init__(self):
        Default.__init__(self)
        self._thr   = None
        self.orig   = ""
        self.result = []
        self.txt    = ""
        self.type = "event"

    def reply(self, txt):
        "add text to the result."
        self.result.append(txt)


def __dir__():
    return (
        'EVent',
    )
