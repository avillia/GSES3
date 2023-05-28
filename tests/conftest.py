from os import path
from os import remove as remove_file

from pytest import fixture


@fixture
def sample_db():
    create_test_db_instance()

    yield

    teardown_test_db_instance()


def create_test_db_instance():
    create_csv_file("test_db.csv")


def create_csv_file(filename: str):
    with open(filename, "w"):
        ...


def teardown_test_db_instance():
    remove_csv_file("test_db.csv")


def remove_csv_file(filename: str):
    if path.exists(filename):
        remove_file(filename)
