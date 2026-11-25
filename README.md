# ShopSphere — AI-Powered E-Commerce (Zero to Production)

ShopSphere is the educational, full-stack e-commerce project developed step by step in the **Nilesh Technology — AI Ecommerce: Zero to Production** series. We will implement a customer storefront, administration workflows, a Python API, PostgreSQL storage, payment integration, and AI-powered shopping features over successive episodes.

> **Current progress (Episode 014):** The repository and design documents were introduced in Episode 013. Episode 014 creates the initial FastAPI application and a process-level `/health` endpoint. The React frontend, PostgreSQL integration, authentication, payments, AI, and deployment are **not yet implemented**.

## Technologies (planned)

| Layer       | Technology                        | Current state                |
| ----------- | --------------------------------- | ---------------------------- |
| Backend API | Python, FastAPI, Uvicorn          | Initial setup in Episode 014 |
| Frontend    | React, TypeScript, Vite           | Planned for a later episode  |
| Database    | PostgreSQL, SQLAlchemy, Alembic   | Planned                      |
| Payment     | Razorpay                          | Planned                      |
| AI          | LLMs, embeddings, semantic search | Planned                      |
| Deployment  | Docker, AWS, CI/CD                | Planned                      |

## Repository layout

```text
ai-ecommerce/
├── README.md              # This project overview
├── backend/
│   ├── README.md          # Backend installation and run guide
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       └── main.py
├── frontend/
│   └── README.md          # Frontend setup guide (not installed yet)
├── docs/                  # BRD, SRS, HLD, LLD, ERD and course notes
├── infra/                 # Future infrastructure configuration
├── .gitignore
└── .env.example
```

Some directories or files may be introduced gradually in later lessons. `backend/.venv/` is a local environment that must remain outside Git.

## Where to start

1. Clone or open the **existing** `ai-ecommerce` repository in VS Code; don't run `git init` again if it is already a Git repository.
2. For **Python/FastAPI installation, dependencies, starting the server, and testing `/health`**, read [`backend/README.md`](backend/README.md).
3. For **React/TypeScript prerequisites, frontend initialization, and development commands once implemented**, read [`frontend/README.md`](frontend/README.md).
4. Review the design artifacts in `docs/` before modifying API contracts or database schemas.
5. Never commit a real `.env`, API key, payment key, credential, or `backend/.venv/`.

## Run the project

**Backend (available after Episode 014 setup):** See [`backend/README.md`](backend/README.md). Its local API will use `http://127.0.0.1:8000`, and its interactive documentation will use `http://127.0.0.1:8000/docs` when the server is running.

**Frontend (future episode):** See [`frontend/README.md`](frontend/README.md). There is no functioning React app yet, so frontend installation/run commands are marked as future steps.

## Development workflow

Use small, reviewed commits; keep secrets out of Git; update relevant documentation as implementation changes. In course videos, show actual commands and results rather than presenting unimplemented features as finished.

## Learning sequence

Requirements and architecture → repository setup → FastAPI foundation → PostgreSQL/data access → frontend → authentication → catalog/cart/orders → payments → AI features → tests → deployment.
