## logging configuration
from logging.config import dictConfig
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



## create table

from .db import open_conn, close_conn, create_table
con = open_conn('auth.db')
create_table(con)    
close_conn(con)


## finally load blueprints
from .apis import mod_auth_api
from .views import mod_auth