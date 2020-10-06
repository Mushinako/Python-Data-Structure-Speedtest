#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

set_rand_setup = rf"""
import random

test_element = list(range({PARAM}))
random.shuffle(test_element)
s_r = set(test_element)
x = False

def test_set_rand():
    for e in s_r:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(set_rand_setup)
t = timeit.timeit("test_set_rand()", setup=set_rand_setup, number=TEST_NUM)
s = f"Set R : {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
