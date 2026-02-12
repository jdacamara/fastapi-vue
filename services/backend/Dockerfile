# ---------- Builder ----------
FROM python:3.14-alpine AS builder

WORKDIR /app

# Install build tools (required on Alpine)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Install Poetry
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

# Disable venv creation
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --only main --no-root

# ---------- Runtime ----------
FROM python:3.14-alpine

WORKDIR /app

# Copy installed Python packages
COPY --from=builder /usr/local /usr/local

# Copy app code
COPY src ./src

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
