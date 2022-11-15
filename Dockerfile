FROM python:3

RUN adduser pyuser

USER pyuser

WORKDIR /usr/src/app

COPY requirements3.txt ./
RUN pip install --no-cache-dir -r requirements3.txt

COPY ./*.py .

CMD [ "python", "./server.py" ]