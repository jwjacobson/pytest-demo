from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_index_get_happy():
    response = client.get("/")

    assert response.status_code == 200
    assert "Contact us" in response.text
    assert "Enter your info below" in response.text
    assert "Name" in response.text
    assert "Email" in response.text


def test_index_post_happy():
    form_data = {
        "name": "Abe Simpson",
        "email": "abe@simpson.com",
    }
    
    response = client.post("/", data=form_data)
    
    assert response.status_code == 200
    assert "Thank you, Abe Simpson!" in response.text
    assert "contact you at abe@simpson.com" in response.text
    assert "Go back" in response.text

