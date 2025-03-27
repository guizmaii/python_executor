# Python-Executor

## Project info

- Project started with `uv` package manager (to avoid having to deal with pip madness)     
  See https://docs.astral.sh/uv/ 

## Run the API locally  

```bash
uv run -- flask --app executor run -p 3000
```

## Build & Push Docker image

```bash
export VERSION=<version>
docker build -t guizmaii/python_executor:${VERSION} .
docker push guizmaii/python_executor:${VERSION}
```

## Run Docker image

```bash
export VERSION=<version>
docker run -p 3000:3000 guizmaii/python_executor:<version>
```

## Published Docker images

Docker images are published here: https://hub.docker.com/r/guizmaii/python_executor
