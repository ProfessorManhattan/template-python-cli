FROM python:3.9.4-slim-buster

# Install dependencies (pip)
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install .

# Copy project
COPY . .

LABEL maintainer="{{Author}} <{{Email}}>" \
      version="1.0.0"

# Set up entrypoint
ENTRYPOINT ["python", "run.py"]
