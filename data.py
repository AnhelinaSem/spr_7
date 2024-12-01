import requests

def test_create_courier():
    # Генерируем уникальные данные для нового курьера
    login_pass = register_new_courier_and_return_login_password()
    login, password, first_name = login_pass

    # Проверяем, что курьер успешно создан
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data={
        "login": login,
        "password": password,
        "firstName": first_name
    })
    assert response.status_code == 201
    assert response.json()["ok"] == True

    # Проверяем, что нельзя создать курьера с тем же логином
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data={
        "login": login,
        "password": password,
        "firstName": first_name
    })
    assert response.status_code == 409

def test_login_courier():
    # Генерируем и регистрируем нового курьера
    login_pass = register_new_courier_and_return_login_password()
    login, password, first_name = login_pass

    # Пытаемся авторизоваться с правильными данными
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={
        "login": login,
        "password": password
    })
    assert response.status_code == 200
    assert "id" in response.json()

    # Пытаемся авторизоваться с неправильным паролем
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={
        "login": login,
        "password": "wrongpassword"
    })
    assert response.status_code == 404

def test_create_order():
    # Создаем заказ с указанием цвета
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data={
        "color": ["BLACK"]
    })
    assert response.status_code == 201
    assert "track" in response.json()

    # Создаем заказ без указания цвета
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data={})
    assert response.status_code == 201
    assert "track" in response.json()

def test_list_orders():
    # Получаем список заказов
    response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
    assert response.status_code == 200
    assert "orders" in response.json()
