# ShopSphere Backend — FastAPI

The `backend/` folder contains the ShopSphere Python API. Episode 014 introduces the application, a virtual environment, FastAPI installation, Uvicorn, and the first health endpoint.

## Requirements

- Windows 10/11, PowerShell, and VS Code (the course's recording environment)
- Python 3.13 recommended for this lesson, if installed
- Git (for the existing repository)
- Internet connectivity for dependency installation

The commands below assume you opened a PowerShell terminal at the **repository root** (`ai-ecommerce/`). Confirm this with `Get-Location`.

## 1. Check Python

```powershell
python --version
py -0p
py -3.13 --version
```

The Windows Python launcher may point to a different interpreter from `python`. If Python 3.13 is unavailable, choose an installed, supported Python version and adjust the venv creation command below.

## 2. Create the virtual environment

```powershell
py -3.13 -m venv .\backend\.venv
.\backend\.venv\Scripts\python.exe --version
.\backend\.venv\Scripts\python.exe -m pip --version
```

For a verified alternative Python interpreter:

```powershell
python -m venv .\backend\.venv
```

No PowerShell activation is required: we call the virtual environment's Python executable directly. Do **not** commit `.venv/` to Git.

## 3. Install backend dependencies

Ensure `backend/requirements.txt` contains:

```text
fastapi[standard]
```

Then run at the repository root:

```powershell
.\backend\.venv\Scripts\python.exe -m pip install -r .\backend\requirements.txt
.\backend\.venv\Scripts\python.exe -m pip show fastapi
.\backend\.venv\Scripts\python.exe -m pip show uvicorn
```

Versions shown on your computer are authoritative; they may differ from the course recording.

## 4. Run the API

From the repository root:

```powershell
.\backend\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload --host 127.0.0.1 --port 8000
```

Keep the terminal open. The `--reload` flag is for **local development**, not production.

| URL                                  | Purpose                                   |
| ------------------------------------ | ----------------------------------------- |
| `http://127.0.0.1:8000/health`       | Process-level health endpoint             |
| `http://127.0.0.1:8000/docs`         | Swagger UI, interactive API documentation |
| `http://127.0.0.1:8000/openapi.json` | OpenAPI schema                            |

Expected output for `GET /health`:

```json
{ "status": "ok", "service": "shopsphere-api" }
```

This **does not** check PostgreSQL connectivity or dependent services. Those integrations arrive in later episodes.

Stop the development server with **Ctrl+C**. If port 8000 is already in use, change `--port 8000` to an available port such as `8001`, and adjust the browser URLs accordingly.

## Current source files

```text
backend/
├── README.md
├── requirements.txt
└── app/
    ├── __init__.py
    └── main.py
```

`app/main.py` creates the FastAPI `app` and defines `GET /health`.

## Troubleshooting

- **`py -3.13` not found:** run `py -0p`; select an installed interpreter and re-create the venv using its path.
- **`ModuleNotFoundError: fastapi`:** run `pip install` through `backend/.venv/Scripts/python.exe`, not a different/global Python installation.
- **`Error loading ASGI app`:** verify `backend/app/main.py` exists, exports `app`, and run the documented Uvicorn command from the repository root.
- **Port in use:** use a different `--port`, then update your browser address.
- **PowerShell activation restricted:** direct execution of `.venv/Scripts/python.exe` avoids the activation script.
- **Dependency installation fails:** check internet/network, read the actual error, and retry only after correcting the cause.

## Future work (not included in Episode 014)

PostgreSQL, SQLAlchemy models, Alembic migrations, authentication and authorization, product/cart/order APIs, payments, integration testing, AI features, and production configuration.

Return to the [project overview](../README.md).

## Episode 015 — FastAPI GET APIs, Parameters & Testing

### Install application dependencies (from repository root)

.\backend\.venv\Scripts\python.exe -m pip install -r .\backend\requirements.txt

### Install development/test dependencies (from repository root)

.\backend\.venv\Scripts\python.exe -m pip install -r .\backend\requirements-dev.txt

### Start API (from repository root)

.\backend\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload --host 127.0.0.1 --port 8000

### Test API (separate terminal)

.\backend\.venv\Scripts\python.exe -m pytest -v backend/tests

### API endpoints

- GET /health: application status
- GET /about: project name and version
- GET /products: in-memory sample catalog; category, in_stock and limit query parameters
- GET /products/{product_id}: one product; HTTP 404 if missing, HTTP 422 if path input invalid
- /docs: interactive OpenAPI (Swagger UI)

The product list is in-memory demo data, not PostgreSQL or production persistence.
