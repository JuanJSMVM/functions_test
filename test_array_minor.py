from array_minor import find_minor

def test_funcion():
    assert find_minor([99,1111,2322,2312321])==99
    assert find_minor([99,1111,2322,21])==21
    assert find_minor([-3223,1111,2322,213745])==-3223
    assert find_minor([100023,12321,23182318])==12321
    assert find_minor([9219,1111,2322,2312321])==1111
