import requests


def test_create_project_positive(headers):
    name = f"test_create_{__name__}_{requests.__version__}"
    payload = {"name": name}
    r = requests.post(
        "https://ru.yougile.com/api-v2/projects",
        json=payload, headers=headers)
    assert r.status_code == 200, f"Ожидался 200, получил {
           r.status_code}: {r.text}"
    data = r.json()
    assert "id" in data
    assert data["name"] == name


def test_update_project_positive(created_project, headers):
    project_id = created_project["id"]
    new_name = f"{created_project['name']}_updated"
    payload = {"name": new_name}
    r = requests.put(
        f"https://ru.yougile.com/api-v2/projects/{
            project_id}", json=payload, headers=headers)
    assert r.status_code == 200, ""
    "Ожидался 200, получил {r.status_code}: {r.text}"
    data = r.json()
    assert data["name"] == new_name


def test_get_project_positive(created_project, headers):
    project_id = created_project["id"]
    r = requests.get(
        f"https://ru.yougile.com/api-v2/projects/{
            project_id}", headers=headers)
    assert r.status_code == 200, ""
    "Ожидался 200, получил {r.status_code}: {r.text}"
    data = r.json()
    assert data["id"] == project_id
    assert "name" in data
