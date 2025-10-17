Flask Blog with Nginx and Docker Compose
=======================================

A minimal blog-style Flask app using SQLite, served by Gunicorn behind Nginx. Run locally via Docker Compose.

Features
--------
- Flask + SQLAlchemy + SQLite
- Create and view blog posts
- Gunicorn app server
- Nginx reverse proxy and static files
- Hot-reload code by bind-mounting the project directory (for local dev)

Quickstart
----------
1. Build and start containers:

```bash
cd /home/roar/Code/trailing
docker compose up --build
```

2. Open the site at `http://localhost:8080`.

3. Create a post at `http://localhost:8080/new`.

Project Structure
-----------------
- `app/` – Flask application package
  - `models.py` – SQLAlchemy models
  - `routes.py` – Flask routes
  - `templates/` – Jinja2 templates
  - `static/` – CSS and assets
- `wsgi.py` – Gunicorn entry point (`wsgi:app`)
- `requirements.txt` – Python dependencies
- `Dockerfile` – App image
- `nginx/` – Nginx Dockerfile and config
- `docker-compose.yml` – Orchestrates app and nginx

Environment
-----------
- `SECRET_KEY` – Flask secret key (default: `dev-secret-key`)
- `DATABASE_URL` – SQLAlchemy DSN (default: `sqlite:////data/blog.db` in the app container)

SQLite DB is persisted to a Docker volume `app-data`.

Common Commands
---------------
- Rebuild after changes:

```bash
docker compose build --no-cache && docker compose up
```

- Tear down:

```bash
docker compose down -v
```

Notes
-----
- Static files are served by Nginx from `/app/app/static/`.
- For real deployments, set a strong `SECRET_KEY` and consider a managed database.


