from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Import config
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Import blueprints
    from mod_auth import mod_auth, mod_auth_api
    app.register_blueprint(mod_auth, url_prefix='/auth')
    app.register_blueprint(mod_auth_api, url_prefix='/api/auth')

    return app




if __name__ == '__main__':      # Use for testing
    test_config = {
        'SECRET_KEY':'WhySoSecret',
        'TESTING':True,
        'DEBUG':True,
        'ENV':'development'
    }
    app = create_app(test_config)
    app.run(host='0.0.0.0', port=8000)
