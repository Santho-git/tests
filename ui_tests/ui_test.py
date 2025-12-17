import requests
import pytest

BASE_URL = "https://reqres.in/api"

def skip_if_cloudflare(response):
    if response.status_code == 403:
        pytest.skip("Blocked by Cloudflare CAPTCHA")

def test_get_users_success():
    response = requests.get(f"{BASE_URL}/users?page=2")
    skip_if_cloudflare(response)
    assert response.status_code == 200

def test_get_single_user_content():
    response = requests.get(f"{BASE_URL}/users/2")
    skip_if_cloudflare(response)

    json_data = response.json()
    assert "data" in json_data
    assert json_data["data"]["id"] == 2

def test_login_missing_password():
    payload = {"email": "abc@company"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    skip_if_cloudflare(response)

    assert response.status_code == 400
    assert "error" in response.json()
