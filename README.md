# Flask Blog with Modern UI & Admin Panel

A full-featured blog application built with Flask, featuring user authentication, admin panel, and modern Tailwind CSS styling. Deployed with Docker Compose and Nginx.

## ✨ Features

### Core Blog Features
- **Blog Posts**: Create, view, and manage blog posts
- **User Authentication**: Registration, login, and logout
- **User Management**: Admin panel for user administration
- **Modern UI**: Beautiful dark theme with Tailwind CSS
- **Responsive Design**: Mobile-friendly interface

### Technical Features
- **Flask + SQLAlchemy**: Robust web framework with ORM
- **SQLite Database**: Lightweight database with persistent storage
- **Flask-Login**: Secure user session management
- **Admin Panel**: User and post management interface
- **Docker Compose**: Easy deployment and development
- **Nginx**: Reverse proxy and static file serving
- **Tailwind CSS**: Modern utility-first CSS framework
- **Hot Reload**: Development-friendly with bind mounts

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Installation

1. **Clone and navigate to the project:**
```bash
git clone <repository-url>
cd trailing
```

2. **Start the application:**
```bash
docker compose up --build
```

3. **Access the application:**
- **Blog**: http://localhost:8080
- **Admin Panel**: http://localhost:8080/admin (login required)

### First Steps

1. **Register an account** at http://localhost:8080/auth/register
2. **Login** at http://localhost:8080/auth/login
3. **Create your first post** at http://localhost:8080/new
4. **Access admin panel** at http://localhost:8080/admin

## 📁 Project Structure

```
trailing/
├── app/                          # Flask application
│   ├── __init__.py              # App factory and configuration
│   ├── models.py                # SQLAlchemy models (User, Post)
│   ├── routes.py                # Blog routes
│   ├── auth.py                  # Authentication routes
│   ├── admin.py                 # Admin panel routes
│   ├── templates/               # Jinja2 templates
│   │   ├── base.html           # Base template with navigation
│   │   ├── index.html          # Blog homepage
│   │   ├── post.html           # Individual post view
│   │   ├── new.html            # Create new post
│   │   ├── auth/               # Authentication templates
│   │   └── admin/              # Admin panel templates
│   └── static/                 # Static assets
│       └── dist/               # Compiled Tailwind CSS
├── nginx/                       # Nginx configuration
│   ├── Dockerfile              # Nginx container
│   └── default.conf            # Nginx configuration
├── src/                         # Tailwind CSS source
│   └── input.css               # Tailwind directives and custom styles
├── package.json                # Node.js dependencies for Tailwind
├── tailwind.config.js          # Tailwind configuration
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Flask app container
├── docker-compose.yml          # Multi-container orchestration
└── wsgi.py                     # Gunicorn entry point
```

## 🎨 UI Features

### Design System
- **Dark Theme**: Professional dark color scheme
- **Tailwind CSS**: Utility-first CSS framework
- **Custom Components**: Reusable button and form styles
- **Responsive Layout**: Mobile-first design approach

### Pages & Features
- **Homepage**: Clean blog post listing
- **Post View**: Individual post with author information
- **Authentication**: Modern login/register forms
- **Admin Dashboard**: Statistics and quick actions
- **User Management**: Admin interface for user roles
- **Post Management**: Admin interface for content management

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key (default: `dev-secret-key`)
- `DATABASE_URL`: Database connection string (default: `sqlite:////data/blog.db`)

### Database
- **SQLite**: Default database for development
- **Persistent Storage**: Data stored in Docker volume `app-data`
- **Migrations**: Flask-Migrate for database schema changes

## 🛠️ Development

### Common Commands

**Start development:**
```bash
docker compose up --build
```

**Rebuild after changes:**
```bash
docker compose build --no-cache && docker compose up
```

**Stop and clean up:**
```bash
docker compose down -v
```

**View logs:**
```bash
docker compose logs -f
```

### CSS Development
The project uses Tailwind CSS with custom configuration:

```bash
# Build CSS (happens automatically in Docker)
npm run build-css-prod

# Watch mode for development
npm run build-css
```

## 🔐 Security Features

- **Password Hashing**: Secure password storage with Werkzeug
- **Session Management**: Flask-Login for user sessions
- **Admin Protection**: Role-based access control
- **CSRF Protection**: Built-in Flask CSRF protection
- **Input Validation**: Form validation and sanitization

## 📊 Admin Panel

### Dashboard
- User and post statistics
- Recent posts overview
- Quick action buttons

### User Management
- View all users
- Toggle admin privileges
- User role management

### Post Management
- View all posts
- Delete posts
- Post content preview

## 🚀 Deployment

### Production Considerations
1. **Set strong SECRET_KEY** in environment variables
2. **Use PostgreSQL** for production database
3. **Configure proper logging**
4. **Set up SSL/TLS certificates**
5. **Use environment-specific configurations**

### Docker Production
```bash
# Set production environment
export SECRET_KEY="your-production-secret-key"
export DATABASE_URL="postgresql://user:pass@host:port/db"

# Build and deploy
docker compose -f docker-compose.prod.yml up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Flask, Tailwind CSS, and Docker**


