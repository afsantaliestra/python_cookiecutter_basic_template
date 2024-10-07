# {{ cookiecutter.project_name }}

## Using this repository

- Install Pyenv -> [GitHub](https://github.com/pyenv/pyenv)
    - With Pyenv install Python 3.12.6 -> `pyenv install 3.12.6`
- User Python 3.12.6 on the root path of this repository -> `pyenv local 3.12.6`
- Install hatch -> `pip install hatch`
- Run the comands in the makefile.
    - `make help` -> Display help and exit.
    - `make lint` -> Perform formating and linting with Ruff.
    - `make mkdocs` -> Serve MkDocs documentation.
    - `make build_doc` -> Build static site of the doc.
    - `make pre_commit` -> Add pre-commit hooks to git-commit.
    - `make hello_world` -> Launch a hello world program.

## VSCode recomendations

### Extensions

- Python
- Python Debugger
- Pylance
    - In Pylance is recommended to activate (already activated in this repo):
        - `"python.analysis.autoImportCompletions": true`
        - `"python.analysis.importFormat": "absolute"`
        - `"python.analysis.indexing": true`
- Ruff
- Git Graph
- Makefile Tools

### Windows Extensions

- WSL
