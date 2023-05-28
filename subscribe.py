from csv import reader as read_as_csv
from csv import writer


def subscribe(email: str) -> bool:
    if _check_if_db_already_contains(email):
        raise ValueError(f"{email} e-mail is already in a db!")
    return _append_db_with(email)


def _check_if_db_already_contains(email: str) -> bool:
    records = _retrieve_all_email_records()
    return email in records


def _append_db_with(email: str) -> bool:
    try:
        _write_to_db(email)
        return True
    except Exception:
        # Since this interface is unaware of db backend we use,
        # Exception is broad and generalized
        return False


def _retrieve_all_email_records() -> list[str]:
    with open("db.csv", "r") as file:
        raw_data = read_as_csv(file)
        lines = list(raw_data)
        return _flatten(lines)


def _flatten(lines: list[list[str]]) -> list[str]:
    return list(*zip(*lines))


def _write_to_db(email: str):
    with open("db.csv", "a", newline="") as file:
        writer(file).writerow([email])
