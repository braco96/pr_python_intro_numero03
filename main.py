# -*- coding: utf-8 -*-
import re
def dedup(seq):
    res = []
    for x in seq:
        if x not in res:
            res.append(x)
    return res

