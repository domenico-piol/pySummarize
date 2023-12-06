FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

RUN pip install torch transformers flask pyopenssl

ADD fb-bart-large-cnn fb-bart-large-cnn/
ADD summarize.py summarize.py

ENTRYPOINT [ "python", "summarize.py"]