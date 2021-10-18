FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL MAINTAINER="MFurquim Dev <mateus@mfurquim.dev>"

EXPOSE 8000

COPY requirements.txt /app/

RUN apt-get update \
  && apt-get install -y build-essential python3-pip python3-dev gcc musl-dev libffi-dev libssl-dev make libpq-dev \
  && pip3 install -U pip setuptools wheel \
  && pip3 install gunicorn uvloop httptools \
  && pip3 install -r /app/requirements.txt \
  && rm -rf /root/.cache/

COPY ./app /app/app
COPY ./asgi.py /app

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}

ENTRYPOINT /usr/local/bin/gunicorn \
	-b 0.0.0.0:8000 \
	-w 4 \
	-k uvicorn.workers.UvicornWorker asgi:app \
	--chdir /app \
	--access-logfile "$ACCESS_LOG" \
	--error-logfile "$ERROR_LOG"
