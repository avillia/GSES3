from assertpy import assert_that

from api.db import append_db_with, retrieve_all_emails
from tests.utils import generate_sample_string


def test_writing_values(sample_db):
    db_name = "test_db.csv"

    emails = [generate_sample_string() for _ in range(100)]

    for email in emails:
        append_db_with(email, db_name)

    retrieved = retrieve_all_emails(db_name)

    assert_that(retrieved).is_type_of(list)
    assert_that(retrieved).is_equal_to(emails)
