# DevopsDemo

Test-driven FastAPI service with a GitHub Actions CI/CD pipeline.

## Pipeline

Pull requests run tests, coverage, formatting, linting, dependency auditing, and
a Bandit security scan. Pushes to `develop` or `main` then build and publish a
commit-tagged image to GHCR.

The staging and production validation workflows check out the tested revision,
build it with Docker Compose, start the service, wait for `/health`, run API
smoke tests, upload container logs, and tear it down. Production is protected
by the GitHub `production` environment, so approval rules can be enabled in
repository settings. These are self-contained deployment validations, not
deployments to a public server.

## Run locally

```bash
pip install -r app/requirements.txt
PYTHONPATH=. uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`, with interactive
documentation at `/docs`.

## Build the container

```bash
docker build --tag fastapi-app ./app
docker run --publish 8000:8000 fastapi-app
curl http://localhost:8000/health
```

## Validate with Docker Compose

```bash
docker compose --file infra/docker-compose.yml build
docker compose --file infra/docker-compose.yml up --detach
curl http://localhost:8000/health
docker compose --file infra/docker-compose.yml logs
docker compose --file infra/docker-compose.yml down --volumes
```
