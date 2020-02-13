import pytest

from examples.identifier import Identifier


@pytest.mark.parametrize('id, is_valid', [
    ('', False),
    ('a', True),
    ('ab', True),
    ('abcde', True),
    ('abcdef', True),
    ('abcdefg', False),
    ('1a', False),
    ('a1', True),
    ('açaí', False),
])
def test_valid_identifier(id, is_valid):
    identifier = Identifier()
    identifier_is_valid = identifier.validate_identifier(id)
    assert identifier_is_valid is is_valid
