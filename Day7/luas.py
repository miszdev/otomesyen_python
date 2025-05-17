import pytest

def luas_lingkaran(r):
  return 3.14 * r**2

input = [
  (10, 314.0),
  (1, 3.14),
  (0, 0),
  (2, 12.56)
]

@pytest.mark.parametrize('r, a', input)
def test_luas(r, a):
  jari = r
  luas = luas_lingkaran(jari)
  assert luas == a