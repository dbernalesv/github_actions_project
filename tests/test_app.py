import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_home_page_returns_application_content(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Aplicación Flask lista" in response.get_data(as_text=True)


def test_health_endpoint_reports_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
