FROM ubuntu:18.04 AS setup

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    wget build-essential zlib1g-dev libssl-dev libsqlite3-dev

WORKDIR /install

# Download Python 3.10 and build from source
# (if we use an Ubuntu package we only get version 3.6)
RUN wget -q https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
RUN tar xzf Python-3.10.4.tgz
RUN rm Python-3.10.4.tgz
RUN cd Python-3.10.4 && ./configure && make && make install

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY database.py .
COPY test_database.py .

CMD ["pytest"]
