import argparse
import json

from flask import Flask
import requests
import git


def create_species_handler_app(task_handler_port, task_handler_ip, port):
    global git_sha
    app = Flask(__name__,  instance_relative_config=True)

    url = f"http://{task_handler_ip}:{task_handler_port}/species_handler_register"
    message = {
        'specie_handler_port': port,
        'specie_handler_ip': "127.0.0.1",  # TODO: get it from script
        "git_sha": git_sha
    }
    print(f"url:{url}")
    x = requests.post(url, json=message)
    response_post = json.loads(x.text)
    if response_post["status"] != "correct":
        print(x.text)
        exit(-1)

    print(f"CONNECT RESPONSE {x.text}")

    @app.route('/')
    def hello():
        return 'Hello, World!'
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="port for species_handler app", default=7000, type=int)
    parser.add_argument("--task_handler_port", help="port for species_handler app", default=8000, type=int)
    parser.add_argument("--task_handler_ip", help="port for species_handler app", default="127.0.0.1", type=str)
    cmd_arguments = parser.parse_args()

    repo = git.Repo(search_parent_directories=True)
    git_sha = repo.head.object.hexsha

    app_ = create_species_handler_app(cmd_arguments.task_handler_port, cmd_arguments.task_handler_ip, cmd_arguments.port)
    app_.run(port=cmd_arguments.port)
