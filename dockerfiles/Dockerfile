FROM ubuntu:18.04

WORKDIR /src

RUN apt update -y
RUN apt install -y --no-install-recommends build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
RUN apt install -y python3 python3-pip python3-dev

# COPY requirements.txt .
# RUN pip3 install -r requirements.txt

COPY src/ .

# ENTRYPOINT ["python3"]
ENTRYPOINT ["tail", "-f", "/dev/null"]