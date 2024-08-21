# Customer Attributes Project

This is a Dockerized Django project with PostgreSQL as the database and Django Rest Framework for creating Customer Attributes APIs.

## Prerequisites

Make sure you have Docker and Docker Compose installed on your machine. For installation instructions refer:
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/djazi/customer_attributes.git
    ```

2. Navigate to the project directory:
    ```bash
    cd customer_attributes
    ```

3. create .env file
    ```bash
    cp .env_example .env
    ```
4. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
    or
    ```bash
    docker compose up --build
    ```

The Project application will be available at `http://localhost:8000`.

5. create superuser
    ```bash
    docker compose exec web python manage.py createsuperuser
     ```
     or 
    ```bash
    docker-compose exec web python manage.py createsuperuser
     ```
6. Run Unit Test
    ```bash
    docker compose exec web pytest
     ```

## Apis Documentations

The documentation for all available APIs for the customer attributes system is available at `http://localhost:8000/redoc/` or `http://localhost:8000/swagger_ui/`.
## Environment Variables

This project uses environment variables for configuration. These are loaded from the `.env` file. You should create your own `.env` or copy `.env_example` file file in the project root with the following variables:

```env
POSTGRES_DB=<your-database-name>
POSTGRES_USER=<your-database-user>
POSTGRES_PASSWORD=<your-database-password>
POSTGRES_HOST=db
POSTGRES_HOST=db
```
## 🤝 Contributing
