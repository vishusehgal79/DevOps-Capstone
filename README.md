# Employee DevOps Platform

## Project Overview

This project implements an automated DevOps deployment platform for an Employee Management REST API built using FastAPI and SQLite.

It demonstrates application development, automated testing, Docker containerization, CI/CD automation, Kubernetes orchestration, infrastructure provisioning, monitoring, and security scanning.

## Technology Stack

| Category | Tools |
|---|---|
| Backend | Python, FastAPI |
| Database | SQLite, SQLAlchemy |
| Testing | Pytest |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Container Registry | Docker Hub |
| Orchestration | Kubernetes, Minikube |
| Infrastructure as Code | Terraform |
| Package Management | Helm |
| Monitoring | Prometheus, Grafana |
| Security | Trivy |

## Application Features

- Create employee records.
- Retrieve all employees.
- Retrieve an employee by ID.
- Update employee information.
- Delete employee records.
- Health-check endpoint.
- Prometheus metrics endpoint.
- Interactive API documentation through Swagger UI.

## Project Architecture

1. Developer pushes code to GitHub.
2. GitHub Actions runs automated tests.
3. Docker builds the application image.
4. The image is published to Docker Hub.
5. Trivy scans the Docker image for vulnerabilities.
6. Kubernetes deploys and manages application containers.
7. Terraform provisions Kubernetes resources.
8. Helm manages the application deployment.
9. Prometheus collects application metrics.
10. Grafana visualizes monitoring data.

## Project Structure

```text
DevOps-Capstone/
├── app/
├── tests/
├── docker/
├── kubernetes/
├── terraform/
├── helm/
├── monitoring/
├── screenshots/
├── .github/workflows/
└── README.md
```

## Setup and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/vishusehgal79/DevOps-Capstone.git
cd DevOps-Capstone
```

### 2. Create and Activate Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r app/requirements.txt
```

### 4. Run the Application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Application endpoints:

- Health: `http://localhost:8000/health`
- Swagger UI: `http://localhost:8000/docs`
- Prometheus metrics: `http://localhost:8000/metrics`

### 5. Run Tests

```bash
python -m pytest tests/ -v
```

## Docker

Build the Docker image:

```bash
docker build -t employee-management-api:v1 -f docker/Dockerfile .
```

Run the container:

```bash
docker run -d --name employee-api -p 8000:8000 employee-management-api:v1
```

## Kubernetes

Apply Kubernetes resources:

```bash
kubectl apply -f kubernetes/
```

Check deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

## Terraform

```bash
terraform -chdir=terraform init
terraform -chdir=terraform apply
```

## Helm

```bash
helm lint ./helm/employee-api
helm upgrade --install employee-api-release ./helm/employee-api -n employee-platform
```

## Monitoring

Prometheus collects application metrics from the FastAPI metrics endpoint.

Grafana visualizes:
- HTTP request rate.
- Average API response time.

Monitoring interfaces:

- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3001`

## Security and CI/CD

GitHub Actions automates:
- Dependency installation.
- Automated testing.
- Docker image building.
- Docker Hub publishing.
- Trivy vulnerability scanning.

The workflow is defined in `.github/workflows/ci.yml`.

## Testing

The application includes automated tests for:
- Health check.
- Employee creation.
- Employee listing.
- Employee updates.
- Employee deletion.

## Screenshots and Evidence

The `screenshots/` directory contains evidence of:
- Docker installation and image creation.
- GitHub Actions execution.
- Docker Hub image publishing.
- Kubernetes deployment, scaling, rolling updates and rollback.
- Terraform provisioning.
- Helm deployment.
- Prometheus and Grafana monitoring.
- Application logs.

## Author

**Vishu Sehgal**

GitHub: https://github.com/vishusehgal79

## Conclusion

This project demonstrates an end-to-end DevOps workflow by integrating application development, automated CI/CD, containerization, orchestration, infrastructure automation, monitoring, and security scanning into a single deployment platform.