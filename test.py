import pytest
from export import add

def test_add():
    assert add(2, 3) == 5        # Test case 1: should pass
    assert add(-1, 1) == 0       # Test case 2: should pass
    assert add(0, 0) == 0         # Test case 3: should pass
    assert add(-1, -1) == -2      # Test case 4: should pass
    assert add(100, 200) == 300   # Test case 5: should pass

if __name__ == "__main__":
    pytest.main()