FROM python

RUN useradd -ms /bin/bash  ayedaemon
USER ayedaemon



WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
