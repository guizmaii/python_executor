FROM ghcr.io/astral-sh/uv:debian

COPY . /app

WORKDIR /app

RUN uv sync --frozen

CMD ["uv", "run", "--", "flask", "--app", "executor", "run", "-p", "3000"]