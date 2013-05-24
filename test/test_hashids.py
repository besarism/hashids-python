from hashids import Hashids

def test_empty_call():
    assert Hashids().encrypt() == ''

def test_default_salt():
    assert Hashids().encrypt(1, 2, 3) == 'katKSA'

def test_single_number():
    h = Hashids()
    assert h.encrypt(12345) == 'rGAx'
    assert h.encrypt(1) == 'yE'
    assert h.encrypt(22) == 'B8'
    assert h.encrypt(333) == '7G9'
    assert h.encrypt(9999) == 'zpz5'

def test_multiple_numbers():
    h = Hashids()
    assert h.encrypt(683, 94108, 123, 5) == '6nph8p9duq8u9'
    assert h.encrypt(1, 2, 3) == 'katKSA'
    assert h.encrypt(2, 4, 6) == '5jhof9'
    assert h.encrypt(99, 25) == 'nq4CG'

def test_salt():
    h = Hashids(salt='Arbitrary string')
    assert h.encrypt(683, 94108, 123, 5) == 'q9khp7X9u6BuE'
    assert h.encrypt(1, 2, 3) == 'a7tLSG'
    assert h.encrypt(2, 4, 6) == 'Xbh4fp'
    assert h.encrypt(99, 25) == 'K6nCz'

if __name__ == '__main__':
    test_salt()
