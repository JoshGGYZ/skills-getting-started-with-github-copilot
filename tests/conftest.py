import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy


@pytest.fixture
def client():
    """
    Provides a TestClient with isolated activities state for each test.
    Resets activities to initial state before each test.
    """
    # Store original activities
    original_activities = copy.deepcopy(activities)
    
    # Reset activities to initial state
    activities.clear()
    activities.update(original_activities)
    
    # Create test client
    test_client = TestClient(app)
    
    yield test_client
    
    # Cleanup: reset activities after each test
    activities.clear()
    activities.update(original_activities)
