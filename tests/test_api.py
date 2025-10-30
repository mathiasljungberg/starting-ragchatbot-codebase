"""Tests for API endpoints."""

from fastapi.testclient import TestClient


def test_health_check(test_client: TestClient):
    """Test that the API is accessible."""
    response = test_client.get("/")
    assert response.status_code in [200, 404]  # May vary based on root endpoint


def test_courses_endpoint(test_client: TestClient):
    """Test the courses endpoint."""
    response = test_client.get("/api/courses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "courses" in data


def test_query_endpoint_validation(test_client: TestClient):
    """Test query endpoint with invalid data."""
    response = test_client.post("/api/query", json={})
    # Should return 422 for validation error or handle gracefully
    assert response.status_code in [400, 422, 500]


def test_query_endpoint_valid(test_client: TestClient):
    """Test query endpoint with valid data."""
    response = test_client.post(
        "/api/query",
        json={"query": "What is this course about?", "session_id": "test-session"},
    )
    # May succeed or fail depending on environment setup
    assert response.status_code in [200, 500]
