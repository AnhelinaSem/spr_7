import pytest
import allure


@allure.description(
        'Проверяем создание заказа')
@pytest.mark.parametrize("color", [
    (["BLACK"]),
    (["GREY"]),
    (["BLACK", "GREY"]),
    ([])
])
def test_create_order_with_colors(create_order, color):
    response = create_order(color)
    assert response.status_code == 201
    assert "track" in response.json()

def test_get_orders_list(get_orders_list):
    response = get_orders_list
    assert response.status_code == 200
    assert "orders" in response.json(), "Ответ не содержит ключ 'orders'"
    assert isinstance(response.json()["orders"], list), "Ключ 'orders' не является списком"
