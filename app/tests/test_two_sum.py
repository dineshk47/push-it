from fastapi.testclient import TestClient
from fastapi import FastAPI

from app.problems.router import router


app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_two_sum_success():
    """Test valid input where a pair exists"""
    payload = {"numbers": [2, 7, 11, 15], "target": 9}
    response = client.post("/two-sum", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "indices" in data
    assert data["indices"] == [1, 2]


def test_two_sum_no_pair():
    """Test case where no valid pair adds up to target"""
    payload = {"numbers": [1, 2, 3, 4], "target": 10}
    response = client.post("/two-sum", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data == {"error": "No valid pair found"}


def test_two_sum_single_element():
    """Test with too few elements (no pairs possible)"""
    payload = {"numbers": [5], "target": 5}
    response = client.post("/two-sum", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert "detail" in body
    assert body["detail"][0]["type"] == "too_short"


def test_two_sum_empty_list():
    """Test with empty list"""
    payload = {"numbers": [], "target": 10}
    response = client.post("/two-sum", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert "detail" in body
    assert body["detail"][0]["type"] == "too_short"

def test_two_sum_multiple_pairs():
    """Test with multiple valid pairs — should return the first that matches"""
    payload = {"numbers": [1, 2, 3, 4, 5], "target": 6}
    response = client.post("/two-sum", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "indices" in data
    # The first valid pair should be 1-based indices [1, 5] (1 + 5 = 6)
    assert data["indices"] == [1, 5]
