from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_and_get_meeting():
    payload = {
        "title": "Sprint planning",
        "notes": "Discuss quarterly objectives and assign action items.",
    }
    response = client.post("/meetings/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert "summary" in data

    meeting_id = data["id"]
    get_response = client.get(f"/meetings/{meeting_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == meeting_id


def test_ask_question():
    response = client.post("/ask/", json={"question": "What did we decide?"})
    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "What did we decide?"
    assert "answer" in data
