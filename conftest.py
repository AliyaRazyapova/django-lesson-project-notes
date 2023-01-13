import pytest


@pytest.fixture(autouse=True)
def init_db(db):
    pass