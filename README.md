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

La aplicación estará disponible en <http://127.0.0.1:8080/>. Los endpoints `/health` y `/version` muestran el estado y la versión de compilación. En local, la versión predeterminada es `dev`; la imagen publicada recibe el SHA del commit.

## Construir y ejecutar con Docker

```powershell
docker build -t github_actions_project:local .
docker run --rm -p 8080:8080 github_actions_project:local
```

## CI/CD

El workflow `CI/CD` llama los workflows reutilizables del repositorio público [`github_actions_templates`](https://github.com/dbernalesv/github_actions_templates), fijados a una revisión por SHA.

- En pull requests a `main` y pushes a `main`, ejecuta las pruebas Python.
- Después de que las pruebas pasen en un push a `main`, construye y publica la imagen en Docker Hub con los tags `latest` y `sha-<commit>`.

La publicación recibe los repository secrets `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`. El workflow de pruebas no recibe secretos.
