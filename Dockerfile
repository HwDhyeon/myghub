FROM python:3.9.5


USER root
WORKDIR /root

ENV HOME=/root
ENV GH_TOKEN=1234

COPY *.whl .

RUN apt -y update && \
    apt -y upgrade && \
    apt -y install vim

RUN pip install -U pip
RUN pip install --find-links=/root gh_issue_tracker

CMD [ "uvicorn issue_tracker.server.server:app --port 8000 --host 0.0.0.0" ]
