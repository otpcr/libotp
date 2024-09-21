L I B O P R
===========


**NAME**


   OPR - Object, Persist, Runtime


**DESCRIPTION**


**OPR** contains all the python3 code to program objects in a functional
way. It provides a base Object class that has only dunder methods, all
methods are factored out into functions with the objects as the first
argument. It is called Object Programming (OP), OOP without the
oriented.

""OPR**  allows for easy json save//load to/from disk of objects. It
provides an "clean namespace" Object class that only has dunder
methods, so the namespace is not cluttered with method names. This
makes storing and reading to/from json possible.

**OPR** has all you need to program a unix nackground daemon, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, deferred exception handling to not crash on an error,
and a policy to keep the main loop running above anything else (it is all
threaded so to not block). Client code is intentionally left out.


**INSTALL**


use pip to install this library.

    $ pip install libopr


**AUTHOR**

Bart Thate ``<record11719@gmail.com>``


**COPYRIGHT**


``LIBOPR`` is Public Domain.
