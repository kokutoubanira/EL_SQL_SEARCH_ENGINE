FROM mysql:8.0.17

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc
COPY ./initdb.d /docker-entrypoint-initdb.d
