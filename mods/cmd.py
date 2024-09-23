# This file is placed in the Public Domain.


"availalbe commands."


from otpcr.command import Commands
from otpcr.object    import keys


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))
