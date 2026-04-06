# ─────────────────────────────────────────────────────────────────────────────
# Base image: official Python 3.12 slim variant
# "slim" means Debian-based but with non-essential packages stripped out —
# smaller image, smaller attack surface, faster pulls.
# We pin to 3.12 explicitly rather than using "latest" so the build is
# reproducible and won't break silently when a new Python version ships.
# ─────────────────────────────────────────────────────────────────────────────
FROM python:3.12-slim

# ─────────────────────────────────────────────────────────────────────────────
# Set the working directory inside the container.
# All subsequent commands run relative to this path.
# ─────────────────────────────────────────────────────────────────────────────
WORKDIR /app

# ─────────────────────────────────────────────────────────────────────────────
# Copy the dependencies file first — before the application code.
# Docker builds images in layers. By copying requirements.txt separately,
# Docker can cache the pip install layer and skip it on rebuilds as long as
# requirements.txt hasn't changed. This makes iterative development faster.
# ─────────────────────────────────────────────────────────────────────────────
COPY requirements.txt .

# ─────────────────────────────────────────────────────────────────────────────
# Install Python dependencies.
# --no-cache-dir: don't store the pip download cache inside the image layer,
#                 keeping the final image smaller.
# ─────────────────────────────────────────────────────────────────────────────
RUN pip install --no-cache-dir -r requirements.txt

# ─────────────────────────────────────────────────────────────────────────────
# Copy the rest of the application code into the container.
# This happens after pip install so code changes don't invalidate the
# dependency cache layer.
# ─────────────────────────────────────────────────────────────────────────────
COPY . .

# ─────────────────────────────────────────────────────────────────────────────
# Expose port 5000 — this is documentation only (it doesn't publish the port).
# The actual port binding is defined in docker-compose.yml.
# ─────────────────────────────────────────────────────────────────────────────
EXPOSE 5000

# ─────────────────────────────────────────────────────────────────────────────
# Start the application using Gunicorn.
# --workers 2     : two worker processes (sufficient for a personal site;
#                   a common formula is 2 × CPU cores + 1, but 2 is safe here
#                   given the shared RAM budget on your VPS)
# --bind 0.0.0.0:5000 : listen on all interfaces inside the container on
#                       port 5000, so Docker can route traffic to it
# app:app         : "in the file app.py, find the object named app"
#                   (first 'app' = filename, second 'app' = Flask instance)
# ─────────────────────────────────────────────────────────────────────────────
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:5000", "app:app"]