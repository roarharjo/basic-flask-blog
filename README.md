# basic-flask-blog

A Flask blog with user authentication, an admin panel, and Tailwind CSS. Runs in Docker with Nginx as reverse proxy.

## What it does

- Create, view, and manage blog posts
- User registration and login
- Admin panel for user and post management
- Dark theme, responsive layout

## Stack

- Flask + SQLAlchemy + SQLite
- Flask-Login for sessions
- Tailwind CSS
- Docker Compose + Nginx
- Gunicorn (WSGI)

## Running it

Requires Docker and Docker Compose.

```bash
git clone https://github.com/roarharjo/basic-flask-blog.git
cd basic-flask-blog
docker compose up --build
```

Then open http://localhost:8080.

Default login: `admin` / `admin123`. Change the password after first login.

## Project structure

```
basic-flask-blog/
├── app/                    # Flask application
│   ├── __init__.py         # App factory and config
│   ├── models.py           # User and Post models
│   ├── routes.py           # Blog routes
│   ├── auth.py             # Authentication routes
│   ├── admin.py            # Admin panel routes
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── post.html
│   │   ├── new.html
│   │   ├── auth/
│   │   └── admin/
│   └── static/dist/        # Compiled CSS
├── nginx/
│   ├── Dockerfile
│   └── default.conf
├── src/
│   └── input.css           # Tailwind source
├── package.json
├── tailwind.config.js
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── wsgi.py                 # Gunicorn entry point
```

## Development

```bash
docker compose up --build          # start
docker compose build --no-cache && docker compose up  # rebuild
docker compose down -v             # stop and clean
docker compose logs -f             # tail logs
```

Tailwind builds automatically in Docker. For manual CSS builds:

```bash
npm run build-css-prod    # one-shot
npm run build-css         # watch mode
```

## Admin panel

- Dashboard with user/post counts and recent posts
- User management: list users, toggle admin role
- Post management: list and delete posts

## Configuration

Environment variables (with defaults):

| Variable | Default |
|---|---|
| `SECRET_KEY` | `dev-secret-key` |
| `DATABASE_URL` | `sqlite:////data/blog.db` |
| `ADMIN_USERNAME` | `admin` |
| `ADMIN_PASSWORD` | `admin123` |

The SQLite database persists in the `app-data` Docker volume.

## Security

- Passwords hashed with Werkzeug
- Flask-Login session management
- Role-based admin access
- CSRF protection via Flask

## Production

For production use:

1. Set a strong `SECRET_KEY`
2. Swap SQLite for PostgreSQL
3. Add SSL/TLS
4. Configure logging

## License

MIT
