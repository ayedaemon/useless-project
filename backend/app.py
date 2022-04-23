from flask import Flask


def create_app(test_config=None) -> Flask:

    app = Flask(__name__)

    # Import config
    if test_config is None:
        config_file = 'config.py'
        app.config.from_pyfile(config_file, silent=False)
        app.logger.info(f"config loaded successfully from file: {config_file}")
    else:
        app.config.from_mapping(test_config)
        app.logger.info("User config is loaded successfully!")
        app.logger.debug(app.config)
    
    
    # from pprint import pprint
    # pprint(app.config)


    # Load extensions
    from extensions import db, jwt
    db.init_app(app)
    jwt.init_app(app)



    # Import blueprints
    from blueprints.mod_auth_api import mod_auth_api
    app.register_blueprint(mod_auth_api, url_prefix='/')
    
    # from blueprints.auth_view import mod_view
    # app.register_blueprint(mod_view, url_prefix='/view')

    return app



if __name__ == '__main__':      # Use for testing
    app = create_app()
    app.run(host='0.0.0.0', port=8000)
