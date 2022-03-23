FROM ubuntu:latest
WORKDIR /app
COPY server.py requirements.txt /app/
RUN apt update && apt install python3 python3-pip -y
RUN pip3 install -r requirements.txt
ENV MODEL_PATH=/app/data/deploy
EXPOSE 3000
ENTRYPOINT ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000"]
