def subscribe(email: str) -> bool:
    if _check_if_db_already_contains(email):
        raise ValueError
    return _append_db_with(email)


def _check_if_db_already_contains(email: str) -> bool:
    records = _retrieve_all_email_records()
    return email in records


def _append_db_with(email: str) -> bool:
    try:
        _write_to_db(email)
        return True
    except Exception:
        return False


def _retrieve_all_email_records() -> list[str]:
    ...


def _write_to_db(email: str):
    ...

