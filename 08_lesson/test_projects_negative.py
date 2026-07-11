import requests


def test_create_project_negative_missing_name(headers):
    payload = {}
    r = requests.post(
        "https://ru.yougile.com/api-v2/projects",
        json=payload, headers=headers)
    assert r.status_code in (
        400, 422), f"Ожидался 400/422, получил {
            r.status_code}"


def test_update_project_negative_invalid_id(headers):
    invalid_id = "nonexistent_project_1234567890abcdef"
    payload = {"name": "should_fail"}
    r = requests.put(
        f"https://ru.yougile.com/api-v2/projects/{
            invalid_id}", json=payload, headers=headers)
    assert r.status_code in (
        404, 403), f"Ожидался 404/403, получил {
            r.status_code}"


def test_get_project_negative_invalid_id(headers):
    invalid_id = "nonexistent_project_1234567890abcdef"
    r = requests.get(
        f"https://ru.yougile.com/api-v2/projects/{
            invalid_id}", headers=headers)
    assert r.status_code in (
        404, 403), f"Ожидался 404/403, получил {
            r.status_code}"
