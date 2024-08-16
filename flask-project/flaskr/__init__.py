import os
from flask import Flask
from . import db, auth, blog


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    print(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,
                              'flaskr.sqlite'),
    )
    app.run(port=8000, debug=True)

    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=False)
    # else:
    #     app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World!'

    @app.endpoint('/')
    def index():
        return blog.index()

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    return app
