from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

# test home endpoint
def test_home():
    response = client.get("/")

    # status code checkz
    assert response.status_code == 200

    # response data check
    assert response.json() == {"message": "CORS is enabled for this FastAPI application!"}


# test add endpoint
def test_add():
    response = client.get("/add?a=5&b=3")

    # status code check
    assert response.status_code == 200

    # response data check
    assert response.json() == {"result": 8}