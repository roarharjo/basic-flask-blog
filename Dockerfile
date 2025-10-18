FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential curl && rm -rf /var/lib/apt/lists/*

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# App source
COPY . .

# Install Node dependencies and build Tailwind CSS
RUN npm install
RUN mkdir -p app/static/dist
RUN npm run build-css-prod
RUN ls -la app/static/dist/

# Environment defaults
ENV FLASK_ENV=production \
    SECRET_KEY=dev-secret-key \
    DATABASE_URL=sqlite:////data/blog.db

# Create data dir for sqlite and set permissions
RUN mkdir -p /data && chown -R root:root /data

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app", "--workers", "2", "--threads", "4", "--timeout", "60"]


