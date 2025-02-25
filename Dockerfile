FROM python:3.10.5-slim-buster AS base
LABEL maintainer="rzmobiledev@gmail.com"
ENV PYTHONUNBUFFERED 1

FROM base AS builder
WORKDIR /install
COPY requirements_new.txt .
COPY /core/scripting/ /scripting

RUN apt update \
    && pip install --upgrade pip && pip install --prefix="/install" -r requirements_new.txt && \
    adduser --disabled-password --no-create-home \
    anbk && chmod -R +x /scripting

USER anbk

FROM base
COPY --from=builder  /install /usr/local
COPY --from=builder /scripting /usr/local/bin
WORKDIR /app
COPY . /app

EXPOSE 3001
ENV PATH="/scripting:/usr/local/bin:$PATH"
CMD [ "automation.sh" ]