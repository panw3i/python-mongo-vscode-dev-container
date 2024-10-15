FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

# Install MongoDB command line tools
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends wget gnupg \
    && wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - \
    && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list \
    && apt-get update \
    && apt-get install -y mongodb-org-tools mongodb-org-shell \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN pip3 --disable-pip-version-check --no-cache-dir install pylint