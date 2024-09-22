# This file is placed in the Public Domain.
# pylint: disable=W0622


"package"


import os


__doc__ = __file__.rsplit(os.sep, maxsplit=2)[-2].upper()


from . import client, object, persist, runtime
