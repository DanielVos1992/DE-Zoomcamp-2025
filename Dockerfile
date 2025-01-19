# baseline image for the docker container
FROM python:3.12.8-slim

# Metadata for the container
LABEL description="Docker container for the 2025 cohort - Data engineering Zoomcamp"
LABEL maintainer="Daniel Vos"

RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# installing pandas
RUN pip3 install --no-cache-dir pandas psycopg2-binary jupyter sqlalchemy sqlalchemy_utils

# Set the working directory for the image
WORKDIR /app

