#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

set_setup = rf"""
test_element = range({PARAM})
s = set(test_element)
x = False

def test_set():
    for e in s:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(set_setup)
t = timeit.timeit("test_set()", setup=set_setup, number=TEST_NUM)
s = f"Set   : {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
