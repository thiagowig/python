FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt


ENTRYPOINT ["python3"]
CMD ["main.py"]