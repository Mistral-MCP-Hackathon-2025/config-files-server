# Config Files Server

A minimal FastAPI server to serve versioned configuration files from the local `configs/` directory. Endpoint: `/{version}/{filename}` protected by an `X-API-Key` header.

## Quickstart

1. Create a `.env` file:

```
API_KEY=change-me
```

2. (Optional) Create an example config at `configs/v1/example.yaml`:

```yaml
service:
  name: example
  url: https://api.example.com
  timeout: 10
```

3. Install dependencies (Python 3.13+). Choose one:

- Using pip from the repo root:

```
pip install .
```

- Or install just runtime deps for quick try:

```
pip install fastapi uvicorn[standard] python-dotenv pyyaml httpx
```

4. Run the server:

```
uvicorn app.main:app --reload
```

5. Fetch a file:

```
curl -H "X-API-Key: change-me" http://localhost:8000/v1/example.yaml
```

## Docker

Build the image (from the repo root):

```
docker build -t config-files-server .
```

Run the container, passing the API key and mounting local configs:

```
docker run --rm -p 8000:8000 \
  -e API_KEY=change-me \
  -v "$(pwd)/configs:/app/configs:ro" \
  config-files-server
```

Then fetch a file as before:

```
curl -H "X-API-Key: change-me" http://localhost:8000/v1/example.yaml
```

## Project structure

- `app/` – application code (modularized)
  - `core/` – settings and security
  - `services/` – file storage, utilities
  - `api/routes/` – API routers
- `configs/` – versioned configuration files served by the API
- `scripts/` – utilities and smoke tests

## Notes
- The server prevents path traversal and only serves files within the `configs/` directory.
- The API requires a valid `X-API-Key` header. Set `API_KEY` in `.env`.
