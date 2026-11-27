# github_actions_project

Aplicación web pequeña con Flask, pruebas automatizadas y publicación de una imagen Docker mediante GitHub Actions.

## Ejecutar localmente

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest
python app.py
```

La aplicación estará disponible en <http://127.0.0.1:8080/> y el estado de salud en <http://127.0.0.1:8080/health>.

## Construir y ejecutar con Docker

```powershell
docker build -t github_actions_project:local .
docker run --rm -p 8080:8080 github_actions_project:local
```

## CI/CD

GitHub Actions ejecuta las pruebas y construye la imagen en pull requests y pushes a `main`. Solo los pushes a `main` publican en Docker Hub. El workflow requiere los repository secrets `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`.
