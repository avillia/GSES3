from api.db import append_db_with, retrieve_all_emails


def subscribe(email: str) -> bool:
    if _check_if_db_already_contains(email):
        raise ValueError(f"{email} e-mail is already in a db!")
    return append_db_with(email)


def _check_if_db_already_contains(email: str) -> bool:
    records = retrieve_all_emails()
    return email in records
