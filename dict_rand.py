#!/usr/bin/env python3
import timeit
from common import TEST_NUM, PARAM, FN

dict_rand_setup = rf"""
import random

test_element = list(range({PARAM}))
random.shuffle(test_element)
d_r = {{x: None for x in test_element}}
x = False

def test_dict_rand():
    for e in d_r:
        if e < {PARAM//2}:
            x = True
        else:
            x = False
"""

print(dict_rand_setup)
t = timeit.timeit("test_dict_rand()", setup=dict_rand_setup, number=TEST_NUM)
s = f"Dict R: {t:.6f}"
print(s)
with open(FN, "a") as f:
    print(s, file=f)
