FROM python:3.9-slim
# Docker镜像的名称
# LABEL Name=recordip Version=latest

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pandas requests

CMD ["python", "-u", "RecordIP.py"]