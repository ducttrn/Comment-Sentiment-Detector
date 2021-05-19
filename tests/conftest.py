import pytest

from main.app import app
from tests.utils import MockMemcache


@pytest.fixture(scope="function", autouse=True)
def session():
    # Create app context
    app.app_context().push()

    yield app


@pytest.fixture
def client(session):
    testing_client = session.test_client()

    yield testing_client


@pytest.fixture(autouse=True)
def mock_memcache(mocker):
    mocker.patch("main.engines.evaluate.memcache_client", new_callable=MockMemcache)
