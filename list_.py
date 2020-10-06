#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

list_setup = rf"""
test_element = range({PARAM})
li = list(test_element)
x = False

def test_list():
    for e in li:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(list_setup)
t = timeit.timeit("test_list()", setup=list_setup, number=TEST_NUM)
s = f"List  : {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
