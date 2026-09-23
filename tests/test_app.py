from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert f"Unregistered {email} from {activity_name}" in response.json()["message"]

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]


def test_delete_participant_returns_404_for_missing_activity():
    response = client.delete("/activities/Unknown Activity/participants/test@example.com")

    assert response.status_code == 404
