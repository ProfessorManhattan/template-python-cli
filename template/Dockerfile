# Build BASE image
FROM python:3.10-alpine as base

## Define PYTHON environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Build BUILD image
FROM base as build

## Define PIP and POETRY environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1

## Install OS dependencies, poetry and create virtual environment
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

## Copy settings & dependencies files, then install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

## Build project and install
COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

# Final image
FROM base as final

# Create non-root user
RUN addgroup -g 1000 python && adduser -u 1000 -G python -D python

USER python

## Copy virtual environment, then run
COPY --from=build /venv /venv
COPY app-standalone.py ./

ENTRYPOINT ["/venv/bin/python", "./run.py"]
