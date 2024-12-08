import pytest
from selenium import webdriver
from src.config import Config
import requests
import random
import string
from data import BASE_URL, COURIER_URL, ORDERS_URL

def delete_courier(login, password):
    payload = { "login": login, "password": password }
    response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=payload)
    if response.status_code == 200:
        courier_id = response.json()['id']
        del_response = requests.delete(f'{BASE_URL}{COURIER_URL}/{courier_id}')
        return del_response.status_code == 200
        return False