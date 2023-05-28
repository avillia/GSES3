from assertpy import assert_that

from core.subscribe import subscribe
from tests.utils import generate_sample_string


def test_writing_already_existing_value_raises_error(sample_db):
    email = generate_sample_string()
    subscribe(email)
    email_that_is_already_written = email
    assert_that(subscribe).raises(ValueError).when_called_with(email_that_is_already_written)
