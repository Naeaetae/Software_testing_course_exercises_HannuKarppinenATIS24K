import pytest

from app import InMemoryOrderStore, create_app


@pytest.fixture
def store():
    return InMemoryOrderStore()


@pytest.fixture
def app(store):
    app = create_app(store)
    app.config.update(TESTING=True)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_then_get_order(client, store):
    created = client.post(
        "/orders",
        json={"subtotal_cents": 1250, "discount_percent": 10},
    )
    assert created.status_code == 201
    body = created.get_json()
    assert body["total_cents"] == 1125
    assert store.count() == 1

    fetched = client.get(f"/orders/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.get_json() == body


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount_is_rejected_without_saving(client, store, discount):
    before = store.count()
    response = client.post(
        "/orders",
        json={"subtotal_cents": 1250, "discount_percent": discount},
    )
    assert response.status_code == 400
    assert response.get_json()["error"]["code"] == "invalid_value"
    assert store.count() == before
