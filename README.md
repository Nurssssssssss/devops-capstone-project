# Customer Accounts Microservice

[![Build Status](https://github.com/Nurssssssssss/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Nurssssssssss/devops-capstone-project/actions/workflows/ci-build.yaml)

A Flask-based RESTful microservice for managing customer accounts. It supports
creating, listing, reading, updating, and deleting accounts, with PostgreSQL
persistence, automated tests, security headers, CORS, Docker, and Kubernetes
deployment manifests.

## API
- `GET /health` — service health
- `POST /accounts` — create an account (JSON)
- `GET /accounts` — list accounts
- `GET /accounts/{id}` — read an account
- `PUT /accounts/{id}` — update an account (JSON)
- `DELETE /accounts/{id}` — delete an account

Account JSON fields: `name`, `email`, `address`; optional `phone_number`
and `date_joined` (ISO-8601 date).

## Local setup
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Start PostgreSQL and set `DATABASE_URI` (default:
   `postgresql://postgres:postgres@localhost:5432/postgres`).
4. Run: `honcho start` or `gunicorn --bind 0.0.0.0:8080 wsgi:app`.

## Tests and quality
Run `nosetests -v`, `coverage report -m`, and `flake8 service tests`.

## Container
Build with `docker build -t accounts:1 .`, then run with
`docker run --rm -p 8080:8080 -e DATABASE_URI=<postgres-uri> accounts:1`.

## Kubernetes
Manifests are in `kubernetes/`. Configure the image and database connection
for your cluster before applying them. See `kubernetes/README.md`.

## CI
GitHub Actions runs code checks and the nose test suite on pushes and pull
requests. The badge above reflects the actual latest workflow status.
