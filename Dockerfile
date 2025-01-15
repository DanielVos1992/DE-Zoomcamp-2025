# baseline image for the docker container
FROM python:3.12.8-slim

# Metadata for the container
LABEL description="Docker container for the 2025 cohort - Data engineering Zoomcamp"
LABEL maintainer="Daniel Vos"

# insatlling pandas
RUN pip3 install --no-cache-dir pandas

# Set the working directory for the image
WORKDIR /app

CMD ["python3"]



