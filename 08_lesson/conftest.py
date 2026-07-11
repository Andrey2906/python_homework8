import pytest
import requests
import random
import string

API_KEY = "i5f-St2oy-ZYav3S-CPdPIsRrcrHR3mJTPRp6dZ8vpuJXRKyagLMEgx0dpJ1fe2q"
BASE_URL = "https://ru.yougile.com"


@pytest.fixture(scope="session")
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"YOUGILE-KEY {API_KEY}"
    }


def _random_name(prefix="test_proj_"):
    suffix = "".join(
        random.choices(
            string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}{suffix}"


@pytest.fixture
def created_project(headers):
    name = _random_name()
    payload = {"name": name}
    r = requests.post(
        f"{BASE_URL}/api-v2/projects", json=payload, headers=headers)
    r.raise_for_status()
    data = r.json()
    project_id = data["id"]
    yield {"id": project_id, "name": name}

    try:
        requests.delete(
            f"{BASE_URL}/api-v2/projects/{
                project_id}", headers=headers)
    except Exception:
        pass
