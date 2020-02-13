import pytest

from examples.identifier import Identifier


@pytest.mark.parametrize('id, is_valid', [
    ('a', True),
    ('', False),
    ('abcdefg', False),
    ('1', False),
    ('abcdef', True),
    (' A', False),
    ('123456', False),
    ('çabc', False),
    ('#çabc', False),
    ('a b c', False),
])
def test_valid_identifier(id, is_valid):
    identifier = Identifier()
    identifier_is_valid = identifier.validate_identifier(id)
    assert identifier_is_valid is is_valid
