## Adversarial attack sandbox

### Requirements

* A virtualenv with Python 3.7 or newer ([pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is recommended for managing Python versions and virtualenvs)
* A recent `pip` and `pip-tools` installed inside the virtualenv:
```bash
pip install -U pip
pip install pip-tools
```

### Install Python dependencies

```bash
pip-sync
```

### Add more dependencies

Add name of the package you need to `requirements.in` file, then compile `requirements.txt` and update your venv:
```bash
pip-compile -v -o requirements.txt
pip-sync
```

### Get started

See the [wiki](https://github.com/DariaShel/seminar-at-ispras/wiki).
