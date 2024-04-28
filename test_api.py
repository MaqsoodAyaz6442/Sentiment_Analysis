from fastapi.testclient import TestClient
from main import app
from main import TextInput

client = TestClient(app)

# Test sending a positive sentiment text
def test_positive_sentiment():
    with client:
        # Define the request payload
        payload = TextInput(text="I love this product! It's amazing!")

        # Send a POST request to the sentiment analysis endpoint
        response = client.post("/analyze", json=payload.dict())

        # Assert that the response status code is 200 OK
        assert response.status_code == 200

        # Assert that the sentiment returned is positive
        assert response.json()['sentiment'] == "positive"

# Test sending a negative sentiment text
def test_negative_sentiment():
    with client:
        # Define the request payload
        payload = TextInput(text="I'm really disappointed with this service. It's terrible.")

        # Send a POST request to the sentiment analysis endpoint
        response = client.post("/analyze", json=payload.dict())

        # Assert that the response status code is 200 OK
        assert response.status_code == 200

        # Assert that the sentiment returned is negative
        assert response.json()['sentiment'] == "negative"

# Test sending a neutral sentiment text
def test_neutral_sentiment():
    with client:
        # Define the request payload
        payload = TextInput(text="This is a neutral statement.")

        # Send a POST request to the sentiment analysis endpoint
        response = client.post("/analyze", json=payload.dict())

        # Assert that the response status code is 200 OK
        assert response.status_code == 200

        # Assert that the sentiment returned is neutral
        assert response.json()['sentiment'] == "neutral"
