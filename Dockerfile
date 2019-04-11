FROM python:3.6.0-alpine
RUN pip install codecov pytest-cov pytest-flakes pytest-pep8

ADD . /home/
WORKDIR /home/
