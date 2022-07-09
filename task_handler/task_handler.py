import argparse
from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__,  instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="port for task_handler app", default=8000, type=int)
    cmd_arguments = parser.parse_args()
    app = create_app()
    app.run(port=cmd_arguments.port)
