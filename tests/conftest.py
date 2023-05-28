from os import path
from os import remove as remove_file

from pytest import fixture


@fixture
def sample_db():
    create_test_db_instance()

    yield

    teardown_test_db_instance()


def create_test_db_instance():
    with open("db.csv", "w"):
        ...


def teardown_test_db_instance():
    if path.exists("db.csv"):
        remove_file("db.csv")
