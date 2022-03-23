FROM alpine:latest
WORKDIR /app
COPY main.py requirements.txt /app/
RUN apk add python3 py3-pip
RUN pip3 install -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
