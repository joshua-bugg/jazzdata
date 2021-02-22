from jazzdata.jazzerize import no_boundaries


def test_is_it_jazz():
    assert isinstance(no_boundaries(2, 2), str)
