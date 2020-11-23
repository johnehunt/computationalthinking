from add_function import add

def test_add_zeros():
    result = add(0, 0)
    assert result == 0

def test_add_one_and_zero():
    result = add(1, 0)
    assert result == 1

def test_add_zero_and_one():
    result = add(0, 1)
    assert result == 1

def test_add_one_and_one():
    result = add(1, 1)
    assert result == 2

def test_add_zero_and_minus_one():
    result = add(0, -1)
    assert result == -1

def test_add_minus_one_and_zero():
    result = add(-1, 0)
    assert result == -1

def test_add_minus_one_and_minus_one():
    result = add(-1, -1)
    assert result == -2