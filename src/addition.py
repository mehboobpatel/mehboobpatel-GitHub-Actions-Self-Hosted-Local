# app.py
# This is a test commit
# testing commit
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def test_addsub():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

    assert sub(10, 3) == 7

