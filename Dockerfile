FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pandas requests

CMD ["python", "RecordIP.py"]