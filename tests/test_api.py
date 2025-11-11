from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={"text": "hello"})
    assert response.status_code == 200
    json_data = response.json()
    assert "bot" in json_data
    assert json_data["bot"] == "Hello! How can I help you today?"
