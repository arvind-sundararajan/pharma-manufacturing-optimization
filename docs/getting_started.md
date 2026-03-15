# Getting Started
## Prerequisites
* Docker installed on the system
* Docker Compose installed on the system

## Step 1: Clone the Repository
Clone the pharma-manufacturing-optimization repository using the following command:
```bash
git clone https://github.com/your-username/pharma-manufacturing-optimization.git
```

## Step 2: Build the Docker Images
Build the Docker images using the following command:
```bash
docker-compose build
```

## Step 3: Start the Services
Start the services using the following command:
```bash
docker-compose up
```

## Step 4: Access the API
Access the API using a tool like curl or Postman, using the following URL:
```bash
curl http://localhost:8080/api/optimization
```