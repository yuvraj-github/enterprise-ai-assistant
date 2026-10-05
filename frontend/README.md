# Enterprise AI Assistant

React frontend for asking questions about company policies and viewing
source-backed answers.

## Run locally

Install dependencies and start the Vite development server:

```sh
npm install
npm run dev
```

The frontend connects to `http://127.0.0.1:8000` by default. To use a different
backend URL, set `VITE_API_BASE_URL` in a `.env` file in this directory:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

The API URL is the backend origin; the frontend appends `/api/ask`.

## Production build

```sh
npm run build
```
