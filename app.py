"""Small Flask application for the GitHub Actions CI/CD project."""

import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    """Render the example application's home page."""
    return """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>GitHub Actions Project</title>
  </head>
  <body>
    <main>
      <h1>Aplicación Flask lista</h1>
      <p>CI/CD con GitHub Actions y Docker Hub.</p>
      <p>Estado: <a href="/health">/health</a></p>
      <p>Versión: <a href="/version">consultar versión</a></p>
    </main>
  </body>
</html>"""


@app.get("/health")
def health():
    """Provide a simple health-check response."""
    return jsonify(status="ok")


@app.get("/version")
def version():
    """Expose the version embedded in the built image."""
    return jsonify(version=os.getenv("APP_VERSION", "dev"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
