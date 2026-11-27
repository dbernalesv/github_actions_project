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
    page = response.get_data(as_text=True)
    assert "Aplicación Flask lista" in page
    assert 'href="/version"' in page


def test_health_endpoint_reports_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version_endpoint_reports_build_version(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "test-build-123")

    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json() == {"version": "test-build-123"}
