import argparse
from flask import Flask, request


SPECIES_TASK_LIST = []


def create_task_handler_app():
    app = Flask(__name__,  instance_relative_config=True)

    @app.route('/species_handler_register', methods=('POST',))
    def species_handler_register():
        print(f"{request.json['specie_handler_port']}")
        SPECIES_TASK_LIST.append({"specie_handler_port": request.json['specie_handler_port'],
                                  "specie_handler_ip": request.json['specie_handler_ip']})
        return 'Hello, World!'
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="port for task_handler app", default=8000, type=int)
    cmd_arguments = parser.parse_args()
    app = create_task_handler_app()
    app.run(port=cmd_arguments.port)
