FROM python:3.9

# Update OS and install packages
RUN apt-get update --yes && \
    apt-get dist-upgrade --yes && \
    apt-get install --yes \
      wget \
      zip

ARG DUCKDB_VERSION="0.6.1"
ARG LOCAL_BIN="/sbin"

WORKDIR /

# Install DuckDB CLI
RUN wget https://github.com/duckdb/duckdb/releases/download/v${DUCKDB_VERSION}/duckdb_cli-linux-aarch64.zip --output-document=/tmp/duckdb.zip && \
    unzip /tmp/duckdb.zip -d ${LOCAL_BIN} && \
    rm /tmp/duckdb.zip

ENTRYPOINT ["tail", "-f", "/dev/null"]
