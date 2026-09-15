# DevopsDemo

Test-driven FastAPI service with a GitHub Actions CI/CD pipeline.

## Pipeline

Pull requests run tests, coverage, formatting, linting, dependency auditing, and
a Bandit security scan. Pushes to `develop` or `main` then build and publish a
commit-tagged image to GHCR.

The staging and production workflows start that exact image and run a health
smoke test. Production is protected by the GitHub `production` environment, so
approval rules can be enabled in repository settings.

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
