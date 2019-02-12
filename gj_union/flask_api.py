from flask import Flask


def create_app(debug=False):
    from gj_union import routes
    app = Flask(__name__)
    app.debug = debug
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(routes.bp)
    return app
