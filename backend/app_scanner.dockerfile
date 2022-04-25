FROM python
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . /app
EXPOSE 8000
ENTRYPOINT ["sh", "gunicorn_entry.sh"]