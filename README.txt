Sentiment Analysis API with FastAPI and Hugging Face Transformers

This project implements a sentiment analysis API using FastAPI and integrates a pre-trained model from Hugging Face Transformers. The API accepts JSON input containing a text field and returns the sentiment of the text.

Table of Contents

1. API Development
2. Model Integration
3. Containerization
4. Testing
5. Deployment

API Development

The API is developed using FastAPI and features a POST endpoint /analyze that accepts JSON input containing a text field. It returns the sentiment of the text.

Model Integration

The project utilizes the transformers library from Hugging Face to load a pre-trained sentiment analysis model. The API efficiently handles model loading using FastAPI's background tasks.

Containerization

A Dockerfile is provided to containerize the FastAPI application. The Docker container encapsulates all necessary dependencies and can be built and run locally.

Testing

API testing is performed using FastAPI's TestClient. Three tests are implemented:

Test sending a positive sentiment text.
Test sending a negative sentiment text.

Deployment

The endpoint is deployed on Hugging Face Spaces, allowing for easy access and integration with other platforms.

Setup Instructions

Install Dependencies: Navigate to the project directory and install the required dependencies using pip.
cd project directory
pip install -r requirements.txt

Download Pre-trained Model: The pre-trained model will be automatically downloaded when the application starts.

Build Docker Container: Use the provided Dockerfile to build the Docker container.
docker build -t project_sentiment_analysis .

Run Docker Container: Run the Docker container locally.
docker run -d -p 8000:8000 project_sentiment_analysis .

Access API Documentation: Visit http://localhost:8080/docs to access the API documentation using Swagger UI.
http://localhost:8000/docs#/default/analyze_text_get_analyze_get_post

Test API Endpoints: Use the provided TestClient script (test_client.py) to run API tests.
