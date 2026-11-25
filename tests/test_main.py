import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

# Create a separate temporary test database
test_engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_employee(client):
    response = client.post(
        "/employees",
        json={
            "name": "Rahul Sharma",
            "email": "rahul@example.com",
            "department": "IT",
            "role": "Developer",
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Rahul Sharma"


def test_get_employees(client):
    client.post(
        "/employees",
        json={
            "name": "Priya Sharma",
            "email": "priya@example.com",
            "department": "HR",
            "role": "Manager",
        },
    )

    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_employee(client):
    created = client.post(
        "/employees",
        json={
            "name": "Aman Kumar",
            "email": "aman@example.com",
            "department": "IT",
            "role": "Developer",
        },
    )

    employee_id = created.json()["id"]

    response = client.put(
        f"/employees/{employee_id}", json={"role": "Senior Developer"}
    )

    assert response.status_code == 200
    assert response.json()["role"] == "Senior Developer"


def test_delete_employee(client):
    created = client.post(
        "/employees",
        json={
            "name": "Neha Singh",
            "email": "neha@example.com",
            "department": "Finance",
            "role": "Analyst",
        },
    )

    employee_id = created.json()["id"]

    response = client.delete(f"/employees/{employee_id}")

    assert response.status_code == 200

    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 404
