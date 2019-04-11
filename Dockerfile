FROM python:3.6.0-alpine
RUN pip install codecov pytest-cov pytest-flakes pytest-pep8

ADD main.py /home/
ADD main_tests.py /home/
ADD phonebook.txt /home/
WORKDIR /home/

