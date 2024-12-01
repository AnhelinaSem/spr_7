import requests

class TestCreateCourier:
    def test_create_courier(register_new_courier):
        assert register_new_courier is not None, "Курьер не был создан"

    def test_create_duplicate_courier(register_new_courier):
        login, password, first_name = register_new_courier
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert response.status_code == 409, "Удалось создать двух одинаковых курьеров"

    def test_create_courier_without_required_fields():
        payload = {
            "login": "",
            "password": "",
            "firstName": ""
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert response.status_code == 400, "Запрос без обязательных полей не вернул ошибку"

    def test_create_courier_response_code(register_new_courier):
        assert register_new_courier is not None, "Курьер не был создан"

    def test_create_courier_missing_field():
        payload = {
            "login": "testlogin",
            "password": "testpassword"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert response.status_code == 400, "Запрос без одного из полей не вернул ошибку"

    def test_create_courier_success_response(register_new_courier):
        login, password, first_name = register_new_courier
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json={
            "login": login,
            "password": password,
            "firstName": first_name
        })
        assert response.json().get("ok") == True, "Успешный запрос не вернул {'ok':true}"

    def test_create_courier_duplicate_login(register_new_courier):
        login, password, first_name = register_new_courier
        payload = {
            "login": login,
            "password": "newpassword",
            "firstName": "newname"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert response.status_code == 409, "Запрос с дублирующим логином не вернул ошибку"

