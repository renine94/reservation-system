FROM python:3.12

WORKDIR /app

RUN apt -y update

COPY ..  ./

RUN pip install -r requirements/prod.txt

RUN make test

ENV DJANGO_SETTINGS_MODULE=src.core.settings.prod

# --max-requests 1000 --max-requests-jitter 150 -w $NUM_CORES -k gevent
#CMD sh -c "python manage.py makemigrations --noinput \
#    && python manage.py migrate --noinput \
#    && python manage.py collectstatic --noinput \
#    && gunicorn core.wsgi --bind 0.0.0.0:8000"
CMD make run_prod

EXPOSE 8000
