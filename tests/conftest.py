from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(scope="session")
def initial_activities_snapshot():
    """Capture the initial in-memory activity state once per test session."""
    return deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities(initial_activities_snapshot):
    """Reset mutable global state before each test for full isolation."""
    activities.clear()
    activities.update(deepcopy(initial_activities_snapshot))


@pytest.fixture
def client():
    return TestClient(app)
