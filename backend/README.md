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
