import pytest

from main import app


@pytest.fixture(scope="function", autouse=True)
def session():
    # Create app context
    app.app_context().push()

    yield app


@pytest.fixture
def client(session):
    testing_client = session.test_client()

    yield testing_client
