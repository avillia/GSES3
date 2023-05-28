import random
import string

from assertpy import assert_that

from subscribe import subscribe, _retrieve_all_email_records


def generate_sample_string(length: int = 8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def test_writing_values(sample_db):
    emails = [generate_sample_string() for _ in range(100)]

    for email in emails:
        subscribe(email)

    retrieved = _retrieve_all_email_records()

    assert_that(retrieved).is_type_of(list)
    assert_that(retrieved).is_equal_to(emails)


def test_writing_already_existing_value_raises_error(sample_db):
    emails = [generate_sample_string() for _ in range(10)]

    for email in emails:
        subscribe(email)

    email_that_is_already_written = random.choice(emails)

    assert_that(subscribe).raises(ValueError).when_called_with(email_that_is_already_written)
