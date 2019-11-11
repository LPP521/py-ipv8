from __future__ import division

import os
from functools import reduce


def secure_randint(bitspace):
    delbits = 8 - (bitspace % 8)
    bytez = os.urandom(bitspace // 8)
    if delbits > 0:
        b = (os.urandom(1)[0] & (0xFF >> delbits)).to_bytes(1, 'big', signed=False)
        bytez = b + bytez
    return reduce(lambda a, b: (a << 8) + b, bytez, 0)
