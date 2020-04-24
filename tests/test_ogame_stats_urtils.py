from ogame_stats.utils import nowstr
import string


def test_nowstr():
    """https://stackoverflow.com/a/295146/10124294"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    result = nowstr()
    assert all(c in valid_chars for c in result)
