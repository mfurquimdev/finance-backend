FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL MAINTAINER="MFurquim Dev <mateus@mfurquim.dev>"

COPY ./app /app/app
