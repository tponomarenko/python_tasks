FROM docker.io/ubuntu:22.04

ADD ./script.py /script.py
ADD ./requirements.txt /requirements.txt
ADD ./initialisation.sh /initialisation.sh

RUN bash /initialisation.sh

ENTRYPOINT python3 /script.py
