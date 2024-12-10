import requests
import allure
from data import BASE_URL, COURIER_URL


@allure.description(
        'Проверяем логин курьера')
def test_courier_can_login(register_new_courier):
    login, password, _ = register_new_courier
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 200
    assert "id" in response.json()


def test_login_courier_without_required_fields():
    payload = {
        "login": "",
        "password": ""
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 400
    assert response.json().get('message') == "Недостаточно данных для входа"


def test_login_courier_with_wrong_credentials(register_new_courier):
    login, password, _ = register_new_courier
    payload = {
        "login": login,
        "password": "wrongpassword"
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 404
    assert response.json().get('message') == "Учетная запись не найдена"

    payload = {
        "login": "wronglogin",
        "password": password
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 404
    assert response.json().get('message') == "Учетная запись не найдена"


def test_login_courier_missing_field():
    payload = {
        "login": "testlogin"
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 400, "Недостаточно данных для входа"

    payload = {
        "password": "testpassword"
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 400
    assert response.json().get('message') == "Недостаточно данных для входа"


def test_login_nonexistent_courier():
    payload = {
        "login": "nonexistentlogin",
        "password": "nonexistentpassword"
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 404
    assert response.json().get('message') == "Учетная запись не найдена"


def test_login_courier_returns_id(register_new_courier):
    login, password, _ = register_new_courier
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    assert response.status_code == 200
    assert "id" in response.json()