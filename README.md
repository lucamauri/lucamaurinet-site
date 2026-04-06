# lucamaurinet-site

Personal website for [lucamauri.net](https://lucamauri.net), built with
[Flask](https://flask.palletsprojects.com/) and served via
[Gunicorn](https://gunicorn.org/) inside a Docker container.

This is a personal learning project — its secondary purpose is to serve as a
minimal, well-documented reference for running a Flask app behind Apache on a
shared LAMP server.

---

## Architecture
Internet → Apache:443 (SSL) → proxy_pass → Gunicorn:5000 (Docker) → Flask

- **Apache** handles TLS termination and reverse proxying
- **Gunicorn** is the production WSGI server that runs the Flask app
- **Flask** handles routing and renders Jinja2 HTML templates
- The container binds to `127.0.0.1:5000` only — not reachable from the
  internet directly

---

## Project Structure
```
lucamaurinet-site/
├── docker-compose.yml       # Container orchestration
├── template.env             # Environment variable template (copy to .env)
├── .gitignore
├── README.md                # This file
└── app/
    ├── Dockerfile           # Container image definition
    ├── requirements.txt     # Python dependencies
    ├── app.py               # Flask application and routes
    └── templates/
        ├── base.html        # Master layout (all pages inherit this)
        ├── index.html       # Home page
        └── about.html       # About page
```

---

## Requirements

### Server
- Docker and Docker Compose
- Apache 2.4 with `mod_proxy` and `mod_proxy_http` enabled
- A valid TLS certificate for `lucamauri.net`

### Local development (optional, outside Docker)
- Python 3.12+
- pip

---

## Deployment

### First deployment

**1. Clone the repository**
```bash
git clone https://github.com/lucamauri/lucamaurinet-site.git
cd lucamaurinet-site
```

**2. Create the local environment file**
```bash
cp template.env .env
# Edit .env if you have secrets to add (none required for the base site)
```

**3. Build and start the container**
```bash
docker compose up -d --build
```

**4. Verify the container is running**
```bash
docker compose ps
docker compose logs
```

**5. Enable the Apache vhost**

Deploy `lucamaurinet-le-ssl.conf` to `/etc/apache2/sites-available/`, then:
```bash
sudo a2ensite lucamaurinet-le-ssl.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```

---

### Updating after code changes
```bash
git pull
docker compose up -d --build
```

Docker rebuilds the image and replaces the running container with zero
manual steps.

---

### Stopping the site
```bash
docker compose down
```

---

## Local Development (outside Docker)

For quick iteration on templates and routes without rebuilding the container:
```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The development server starts at `http://localhost:5000`.

> ⚠️ The built-in Flask development server is for local use only.
> Never expose it publicly. Gunicorn is always used in production.

---

## Environment Variables

| Variable    | Description                  | Default      |
|-------------|------------------------------|--------------|
| `FLASK_ENV` | Flask environment mode       | `production` |

Add future secrets (API keys, tokens) to `.env` — never commit that file.

---

## License

[MIT](https://opensource.org/licenses/MIT) — feel free to use this as a
starting point for your own Flask project.