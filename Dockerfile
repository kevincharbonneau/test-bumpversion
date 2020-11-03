FROM python:3.7-slim-buster

RUN mkdir -p /opt/lib/test-bumpversion
WORKDIR /opt/lib/test-bumpversion
RUN python -m pip install --upgrade setuptools
COPY ["src", "tests", "setup.py", "VERSION", "README.md", "./"]

RUN pip install .