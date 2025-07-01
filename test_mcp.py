import requests

def test_provider_info():
    resp = requests.get("http://localhost:8000/provider_info")
    assert resp.status_code == 200
    data = resp.json()
    assert "name" in data
    assert "actions" in data

def test_list_context():
    resp = requests.get("http://localhost:8000/context")
    assert resp.status_code == 200
    items = resp.json()
    assert isinstance(items, list)
    assert len(items) > 0

def test_read_action():
    items = requests.get("http://localhost:8000/context").json()
    if items:
        payload = {"action": "read", "target_id": items[0]["id"]}
        resp = requests.post("http://localhost:8000/action", json=payload)
        assert resp.status_code == 200
        result = resp.json()
        assert result["success"]
