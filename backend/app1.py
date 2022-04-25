from flask import Flask


def load_flask_config(app, test_config=None):
    # Import config
    if test_config is None:
        config_file = 'config.py'
        app.config.from_pyfile(config_file, silent=False)
        app.logger.info(f"config loaded successfully from file: {config_file}")
    else:
        app.config.from_mapping(test_config)
        app.logger.info("User config is loaded successfully!")
        app.logger.debug(app.config)
    
    return app




def load_flask_extensions(app):
    # Load extensions
    from extensions import db
    db.init_app(app)

    from extensions import jwt
    jwt.init_app(app)

    return app





def create_app(test_config=None) -> Flask:

    app = Flask(__name__)

    app = load_flask_config(app, test_config)
    
    app = load_flask_extensions(app)


    # Import blueprints
    from blueprints.mod_auth_api import mod_auth_api
    app.register_blueprint(mod_auth_api, url_prefix='/')
    
    return app



if __name__ == '__main__':      # Use for testing
    app = create_app()
    app.run(host='0.0.0.0', port=8000)
