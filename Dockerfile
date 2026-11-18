FROM python:3.12-slim

WORKDIR /app
COPY . /app

ENV PORT=8080
ENV DOCKER_CONTAINER=1
EXPOSE 8080

CMD ["python3", "server.py", "--no-browser"]
