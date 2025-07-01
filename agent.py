import requests

BASE_URL = "http://localhost:8000"

# Get provider info
def get_provider_info():
    resp = requests.get(f"{BASE_URL}/provider_info")
    print("Provider Info:", resp.json())

# List context items
def list_context():
    resp = requests.get(f"{BASE_URL}/context")
    print("Context Items:", resp.json())
    return resp.json()

# Perform an action
def perform_action(action, target_id, parameters=None):
    payload = {
        "action": action,
        "target_id": target_id,
        "parameters": parameters or {}
    }
    resp = requests.post(f"{BASE_URL}/action", json=payload)
    print(f"Action '{action}' result:", resp.json())
    return resp.json()

if __name__ == "__main__":
    get_provider_info()
    items = list_context()
    if items:
        perform_action("read", items[0]["id"])
