FROM docker.io/ubuntu:22.04
ADD ./script.py /script.py
RUN apt-get --yes update
RUN apt-get --yes install python3 python3-pip ca-certificates
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ENTRYPOINT python3 /script.py
