# Packaged using Docker And Connect
---
## Create Dockerfile
Package the pipeline folder using ```Docker``` (if you have a pipeline folder, otherwise use the folder where you saved it).

```python
FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

COPY ingest_data.py .

ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]
```
### Explanation:
```FROM python:3.13.11-slim```: Start with slim Python 3.13 image for smaller size

```COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/```: Go to the GitHub library to get ```uv``` images

```WORKDIR /code```: Create a folder named "code" inside the container

```ENV PATH="/code/.venv/bin:$PATH"```: Move all libraries from ```uv``` to the top of the PATH addresses

```COPY pyproject.toml .python-version uv.lock ./```: Copy the three folders into the folder inside the container

```RUN uv sync --locked```: Install all libraries in the lock file

```COPY ingest_data.py .```: Copy the processing file into the container

```ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]```: Set entry point to run the ingestion script

## Create DockerImage
Create an image from the previously written Dockerfile.
```python
docker build -t taxi_ingest:v001 .
```
## Connecting containers
Instead of the usual ```docker run -it```, we'll add a few commands to connect to the PostgreSQL container.
```python
docker run -it `
  --network=pg-network `
  taxi_ingest:v001 `
    --pg-user=thanh123 `
    --pg-pass=1234 `
    --pg-host=my_postgres `
    --pg-port=5432 `
    --pg-db=ny_taxi `
    --target-table=yellow_taxi_trips
```
---
### END
