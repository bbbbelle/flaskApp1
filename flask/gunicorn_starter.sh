#!/bin/sh

# gunicorn main:app -c "$PWD"/gunicorn.config.py
# exec "$@"
if [ "$FLASK_DEBUG" = "1" ]; then
    echo "Running on Flask Development Server"
    python3 main.py
else
    echo "Running on gunicorn"
    gunicorn main:app -c "$PWD"/gunicorn.config.py
fi
exec "$@"
