from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_successful():
    response = client.post("/signup", data={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert "Thanks for subscribing" in response.text
