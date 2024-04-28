# FastAPI Dockerized API

This repository contains a FastAPI application Dockerized for easy deployment.

## Instructions

### Build and Run the Docker Container

1. Clone this repository:

    ```bash
    git clone https://github.com/MaqsoodAyaz6442/Sentiment_Analysis
    ```

2. Navigate to the repository directory:

    ```bash
    cd C:\Users\ABC\Downloads\project_sentiment_analysis
    ```

3. Build the Docker image:

    ```bash
    docker build -t project_sentiment_analysis .
    ```

4. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 project_sentiment_analysis .
    ```

   Replace `8000` with the desired host port if needed.

### Interact with the API

- Once the Docker container is running, you can interact with the API using tools like cURL, Postman, or by accessing the provided Swagger UI or ReDoc documentation.

#### Swagger UI

- Open your web browser and navigate to `http://localhost:8000/docs` (replace `8000` with the host port specified during container run).
- You can explore and interact with the API endpoints using the Swagger UI interface.

#### ReDoc

- Open your web browser and navigate to `http://localhost:8000/redoc` (replace `8000` with the host port specified during container run).
- You can explore and interact with the API endpoints using the ReDoc interface.
