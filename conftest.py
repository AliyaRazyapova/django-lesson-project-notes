import pytest

from web.tests.factories import NoteFactory


@pytest.fixture(autouse=True)
def init_db(db):
    pass

@pytest.fixture
def note():
    return NoteFactory()
