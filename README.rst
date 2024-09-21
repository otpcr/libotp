L I B O T P
===========


**NAME**


``OTP`` - Office of the Prosecutor Communication Record 117 of the year 2019 


**DESCRIPTION**


``OTP`` contains all the python3 code to program objects in a functional
way. It provides a base Object class that has only dunder methods, all
methods are factored out into functions with the objects as the first
argument. It is called Object Programming (OP), OOP without the
oriented.

``OTP``  allows for easy json save//load to/from disk of objects. It
provides an "clean namespace" Object class that only has dunder
methods, so the namespace is not cluttered with method names. This
makes storing and reading to/from json possible.

``OTP`` has all you need to program a unix nackground daemon, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, deferred exception handling to not crash on an error,
and a policy to keep the main loop running above anything else (it is all
threaded so to not block). Client code is intentionally left out.


**INSTALL**


``$ pip install libotp``


**AUTHOR**

Bart Thate <``record11719@gmail.com``>


**COPYRIGHT**

``OTP`` is Public Domain.
