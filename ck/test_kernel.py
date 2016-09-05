
import ck.kernel as ck

def test_safe_float():
    import math

    assert ck.safe_float(1, 0) == 1.0
    assert ck.safe_float('a', 0) == 0
    assert ck.safe_float('-5.35', 0) == -5.35
    assert ck.safe_float('Infinity', 0) == float('inf')
    assert math.isnan(ck.safe_float('nan', 0))
