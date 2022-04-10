gunicorn \
    -w 4 \
    -b 0.0.0.0:8000 \
    --log-level=debug \
    --reload \
    "app:create_app()"
