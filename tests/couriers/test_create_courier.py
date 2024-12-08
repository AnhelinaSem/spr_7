import requests
from data import BASE_URL, COURIER_URL
from method.methods import delete_courier
import allure


@allure.description(
        'Проверяем создание курьера')
def test_create_courier(register_new_courier):
    assert register_new_courier is not None


def test_create_duplicate_courier(register_new_courier):
    login, password, first_name = register_new_courier
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
    assert response.status_code == 409, "Этот логин уже используется"


def test_create_courier_without_required_fields():
    payload = {
        "login": "",
        "password": "",
        "firstName": ""
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
    assert response.status_code == 400, "Недостаточно данных для создания учетной записи"


def test_create_courier_missing_field():
    payload = {
        "login": "testlogin432",
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
    assert response.status_code == 400, "Недостаточно данных для создания учетной записи"


def test_create_courier_success_response(register_new_courier):
    login, password, first_name = register_new_courier
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
    if response.status_code == 409:
        login = login + "_new"
        payload["login"] = login
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
    assert response.status_code == 201, f"Курьер не был создан: {response.status_code} - {response.json()}"
    assert response.json() == {"ok": True}, "Ответ не содержит {'ok': True}"
    assert delete_courier(login, password), "Ошибка при удалении курьера"


def test_create_courier_duplicate_login(register_new_courier):
    login, password, first_name = register_new_courier
    payload = {
        "login": login,
        "password": "newpassword",
        "firstName": "newname"
    }
    response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)
    assert response.status_code == 409, "Этот логин уже используется"