import pytest
from selenium import webdriver
from src.config import Config
import requests
import random
import string
from data import BASE_URL, COURIER_URL, ORDERS_URL

@pytest.fixture
def register_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{BASE_URL}{COURIER_URL}', json=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

        # возвращаем список
    return login_pass

@pytest.fixture
def create_order():
    def _create_order(color=None):
        payload = {
            "firstName": "Name",
            "lastName": "Surname",
            "address": "Test Address",
            "metroStation": 4,
            "phone": "+7 800 323 32 32",
            "rentTime": 5,
            "deliveryDate": "2024-12-01",
            "comment": "Test comment",
            "color": color if color else []
        }
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response
    return _create_order

@pytest.fixture
def get_orders_list():
    response = requests.get(f'{BASE_URL}{ORDERS_URL}')
    return response
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    if Config.FULLSCREEN:
        chrome_options.add_argument("--start-maximized")
    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()

