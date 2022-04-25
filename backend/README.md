# Flask-backend


app.py --> Builds the required application using blueprints and models.

### How to spin it up for development? (on linux)

1. execute `bash ./quickstart`...
    - This will start the docker service
    - build the docker image
    - run the container, with port 8000 exposed and current directory mounted in container.
    - Provide a bash shell inside container.

2. When inside container, run
    - `pip install -r requirements.txt`
    - `python app.py`


Now you should be able to check the application running on localhost:8000



----

#### How makefile works here?

TBD

Example:-

```
make app APP_NAME=auth

# Output

build
└── auth
    ├── app.py
    ├── blueprints
    │   └── mod_auth_api
    │       ├── __init__.py
    │       ├── mod_auth_api.py
    │       └── __pycache__
    ├── config.py
    ├── extensions.py
    ├── models
    │   ├── __pycache__
    │   │   └── user.cpython-310.pyc
    │   └── user.py
    └── requirements.txt
```


TLDR;

1. Clean build directory
2. Make `auth` app
3. Make `scanner` app
4. docker-compose the application (for local testing)

```
# Single command for all above steps

make all
```