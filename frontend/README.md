# ShopSphere Frontend — React + TypeScript

The `frontend/` folder will contain the ShopSphere customer-facing React application and, later, the required administration screens.

> **Course status:** Frontend installation is **not part of Episode 014**. The instructions below are for the future React setup lesson. Do not claim that these commands have already been executed or that a frontend server exists yet.

## Planned technology

- React
- TypeScript
- Vite development/build tooling
- React Router and application state/data-fetching libraries, added when required

## Prerequisites (for the frontend setup episode)

Install a supported Node.js LTS version and npm. Check the actual versions and Vite requirements at the time of setup:

```powershell
node --version
npm --version
```

Use VS Code and a PowerShell terminal at the **repository root** (`ai-ecommerce/`).

## Initialize the React application — future lesson only

The following command creates a React/TypeScript Vite project **inside the existing `frontend/` directory**; run it only after verifying the directory contents and the installed Node.js version:

```powershell
Set-Location .\frontend
npm create vite@latest . -- --template react-ts
```

The Vite generator may ask to confirm the destination directory. **Keep this README** and avoid overwriting existing files without reviewing the prompt. If the generator refuses to scaffold a directory that already has files, temporarily move this README aside, scaffold, then merge this documentation back safely. Do not delete course files.

## Install and run — after the frontend has been initialized

From `ai-ecommerce/frontend/`:

```powershell
npm install
npm run dev
```

Open the **actual local URL shown by Vite** (commonly `http://localhost:5173/`; the port can differ). Do not claim the page works until verified in the browser.

## Build and preview — after implementation

```powershell
npm run build
npm run preview
```

`npm run build` uses the configured frontend build scripts. `npm run preview` serves a local build preview; it is not a production deployment.

## Planned folder structure

```text
frontend/
├── README.md
├── package.json           # Created by the frontend setup lesson
├── index.html             # Created by Vite
└── src/                   # React application source
```

The app will eventually include product browsing, categories, cart, checkout, login, account and admin features. These are **planned**, not implemented in Episode 014.

## Frontend environment and security

- Never put server credentials or secret keys into frontend environment variables; browser bundles are public.
- Prefer a development API base URL configured through a documented public environment variable when the React–FastAPI connection is introduced.
- Do not commit `node_modules/`, `dist/`, or real secrets.

## Troubleshooting (once initialized)

- **`npm` not found:** confirm Node.js and npm installation and reopen the terminal.
- **Unsupported Node version:** update to a Node version supported by your chosen Vite release.
- **Port 5173 in use:** follow the actual terminal URL selected by Vite.
- **Frontend can't reach backend:** verify the FastAPI server is running; CORS configuration will be handled during frontend-backend integration.

Return to the [project overview](../README.md).
