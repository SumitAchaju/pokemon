FROM python:3.12.1-alpine

WORKDIR /usr/src/app/

COPY requirements.txt .

RUN \
    apk add --no-cache  postgresql-libs  && \
    apk add --no-cache  --virtual .build-deps gcc musl-dev postgresql-dev  && \
    python3 -m pip install --no-cache-dir -r requirements.txt

RUN  apk --purge del .build-deps

COPY . .

EXPOSE 8000