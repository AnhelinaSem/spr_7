import requests

class TestLoginCourier:

    def test_courier_can_login(register_new_courier):
        login, password, _ = register_new_courier
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 200, "Курьер не смог авторизоваться"
        assert "id" in response.json(), "Успешный запрос не вернул id"

    def test_login_courier_without_required_fields():
        payload = {
            "login": "",
            "password": ""
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 400, "Запрос без обязательных полей не вернул ошибку"

    def test_login_courier_with_wrong_credentials(register_new_courier):
        login, password, _ = register_new_courier
        payload = {
            "login": login,
            "password": "wrongpassword"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 404, "Запрос с неправильным паролем не вернул ошибку"

        payload = {
            "login": "wronglogin",
            "password": password
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 404, "Запрос с неправильным логином не вернул ошибку"

    def test_login_courier_missing_field():
        payload = {
            "login": "testlogin"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 400, "Запрос без пароля не вернул ошибку"

        payload = {
            "password": "testpassword"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 400, "Запрос без логина не вернул ошибку"

    def test_login_nonexistent_courier():
        payload = {
            "login": "nonexistentlogin",
            "password": "nonexistentpassword"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 404, "Запрос с несуществующим пользователем не вернул ошибку"

    def test_login_courier_returns_id(register_new_courier):
        login, password, _ = register_new_courier
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 200, "Курьер не смог авторизоваться"
        assert "id" in response.json(), "Успешный запрос не вернул id"
