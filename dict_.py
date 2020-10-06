#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

dict_setup = rf"""
test_element = range({PARAM})
d = {{x: None for x in test_element}}
x = False

def test_dict():
    for e in d:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(dict_setup)
t = timeit.timeit("test_dict()", setup=dict_setup, number=TEST_NUM)
s = f"Dict  : {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
