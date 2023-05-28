from _csv import reader as read_as_csv, writer


def append_db_with(email: str, db="../db.csv") -> bool:
    try:
        _write_to_db(email, db)
        return True
    except Exception:
        # Since this interface is unaware of db backend we use,
        # Exception is broad and generalized
        return False


def retrieve_all_emails(db="../db.csv") -> list[str]:
    return _retrieve_all_records_from_csv(db)


def _retrieve_all_records_from_csv(db_path: str) -> list[str]:
    with open(db_path, "r") as file:
        raw_data = read_as_csv(file)
        lines = list(raw_data)
        return _flatten(lines)


def _flatten(lines: list[list[str]]) -> list[str]:
    return list(*zip(*lines))


def _write_to_db(email: str, db):
    _write_to_csv_file(email, db)


def _write_to_csv_file(email: str, db_path: str):
    with open(db_path, "a", newline="") as file:
        writer(file).writerow([email])
