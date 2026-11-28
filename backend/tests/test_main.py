import pytest
from fastapi.testclient import TestClient

from backend.app.main import app, INITIAL_PRODUCTS, PRODUCTS

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_demo_products():
    # Keep each test independent: POST, PUT, PATCH and DELETE mutate memory.
    PRODUCTS[:] = [product.model_copy(deep=True) for product in INITIAL_PRODUCTS]


def valid_product():
    return {
        "sku": "KB-001",
        "name": "Mechanical Keyboard",
        "price": 1999.0,
        "category": "Electronics",
        "in_stock": True,
    }


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json()["api_version"] == "0.3.0"


def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_filter_products():
    response = client.get("/products?category=electronics&in_stock=true")
    assert response.status_code == 200
    assert [product["id"] for product in response.json()] == [1]


def test_product_by_id():
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json()["sku"] == "NOTE-001"


def test_missing_product():
    assert client.get("/products/999").status_code == 404


def test_invalid_product_id():
    assert client.get("/products/abc").status_code == 422


def test_invalid_limit():
    assert client.get("/products?limit=0").status_code == 422


def test_create_product_returns_201():
    response = client.post("/products", json=valid_product())
    assert response.status_code == 201
    assert response.json()["id"] == 4
    assert client.get("/products/4").status_code == 200


def test_duplicate_sku_returns_409():
    response = client.post("/products", json={**valid_product(), "sku": "MOUSE-001"})
    assert response.status_code == 409
    assert response.json()["detail"] == "SKU already exists"


def test_invalid_price_returns_422():
    response = client.post("/products", json={**valid_product(), "price": -10})
    assert response.status_code == 422


def test_invalid_sku_returns_422():
    response = client.post("/products", json={**valid_product(), "sku": "bad sku"})
    assert response.status_code == 422


def test_put_replaces_entire_product():
    response = client.put("/products/2", json=valid_product())
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["sku"] == "KB-001"
    assert response.json()["name"] == "Mechanical Keyboard"


def test_put_requires_all_fields():
    assert client.put("/products/2", json={"name": "New Notebook"}).status_code == 422


def test_put_existing_sku_returns_409():
    assert client.put("/products/2", json={**valid_product(), "sku": "MOUSE-001"}).status_code == 409


def test_patch_only_one_field():
    response = client.patch("/products/2", json={"price": 199.0})
    assert response.status_code == 200
    assert response.json()["price"] == 199.0
    assert response.json()["name"] == "Notebook"
    assert response.json()["sku"] == "NOTE-001"


def test_patch_empty_body_returns_422():
    assert client.patch("/products/2", json={}).status_code == 422


def test_patch_null_value_returns_422():
    assert client.patch("/products/2", json={"name": None}).status_code == 422


def test_patch_duplicate_sku_returns_409():
    assert client.patch("/products/2", json={"sku": "MOUSE-001"}).status_code == 409


def test_delete_returns_204_and_removes_product():
    response = client.delete("/products/2")
    assert response.status_code == 204
    assert response.content == b""
    assert client.get("/products/2").status_code == 404


def test_delete_missing_product_returns_404():
    assert client.delete("/products/999").status_code == 404
