from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "ShopSphere backend is running!"}


def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"project": "ShopSphere", "api_version": "0.2.0"}


def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_filter_products():
    response = client.get("/products?category=electronics&in_stock=true")
    assert response.status_code == 200
    assert [p["id"] for p in response.json()] == [1]


def test_product_by_id():
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Notebook"


def test_missing_product():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_invalid_product_id():
    response = client.get("/products/abc")
    assert response.status_code == 422


def test_invalid_limit():
    response = client.get("/products?limit=0")
    assert response.status_code == 422
