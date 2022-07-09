import argparse
from flask import Flask, request
import json
import git

SPECIES_TASK_LIST = []


def create_task_handler_app():
    app = Flask(__name__,  instance_relative_config=True)

    @app.route('/species_handler_register', methods=('POST',))
    def species_handler_register():
        global git_sha
        # The following lines are to check that all connections are from the same git commit to not have any version problem
        if request.json['git_sha'] != git_sha:
            return json.dumps({"status": "error", "error_message": "git_sha_commit_is_not_the_same"})
        print(f"{request.json['specie_handler_port']}")
        SPECIES_TASK_LIST.append({"specie_handler_port": request.json['specie_handler_port'],
                                  "specie_handler_ip": request.json['specie_handler_ip']})
        print(f"list of species tasks: {SPECIES_TASK_LIST}")
        return json.dumps({"status": "correct"})
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="port for task_handler app", default=8000, type=int)
    repo = git.Repo(search_parent_directories=True)
    git_sha = repo.head.object.hexsha

    cmd_arguments = parser.parse_args()
    app = create_task_handler_app()
    app.run(port=cmd_arguments.port)
