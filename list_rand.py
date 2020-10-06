#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

list_rand_setup = rf"""
import random

test_element = list(range({PARAM}))
random.shuffle(test_element)
li_r = list(test_element)
x = False

def test_list_rand():
    for e in li_r:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(list_rand_setup)
t = timeit.timeit("test_list_rand()", setup=list_rand_setup, number=TEST_NUM)
s = f"List R: {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
