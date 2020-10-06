#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

range_setup = rf"""
test_element = range({PARAM})
r = test_element
x = False

def test_range():
    for e in r:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(range_setup)
t = timeit.timeit("test_range()", setup=range_setup, number=TEST_NUM)
s = f"Range : {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
