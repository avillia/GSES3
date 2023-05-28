from os import path


def setup_db():
    if not is_db_exists():
        return create_db()


def is_db_exists():
    return path.exists("db.csv")


def create_db():
    with open("db.csv", "w"):
        ...
