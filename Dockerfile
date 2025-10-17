FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# App source
COPY . .

# Environment defaults
ENV FLASK_ENV=production \
    SECRET_KEY=dev-secret-key \
    DATABASE_URL=sqlite:////data/blog.db

# Create data dir for sqlite and set permissions
RUN mkdir -p /data && chown -R root:root /data

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app", "--workers", "2", "--threads", "4", "--timeout", "60"]


