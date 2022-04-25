from flask import Flask


def load_flask_config(app, test_config=None):
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
    from extensions import jwt
    jwt.init_app(app)

    return app





def create_app(test_config=None) -> Flask:

    app = Flask(__name__)

    app = load_flask_config(app, test_config)
    
    app = load_flask_extensions(app)

    # Import blueprints
    from blueprints.mod_scanner import mod_scanner
    app.register_blueprint(mod_scanner, url_prefix='/scanner')

    return app



if __name__ == '__main__':      # Use for testing
    app = create_app()
    app.run(host='0.0.0.0', port=8000)
