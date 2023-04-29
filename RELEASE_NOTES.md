

### B.O.M.

* Checker :
```bash
poetry --version
python --version
pyenv --version
cookiecutter --version
bash --bersion
```

For this release : 

```bash
$ poetry --version
Poetry (version 1.4.2)


$ python --version
Python 3.10.5


$ pyenv --version
pyenv 2.3.17


$ cookiecutter --version
Cookiecutter 2.1.1 from C:\Users\Utilisateur\.local\pipx\venvs\cookiecutter\lib\site-packages (Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)])


$ bash --version
GNU bash, version 4.4.23(1)-release (x86_64-pc-msys)
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


```

### Install Python 3.10+

See Official Python installation instructions 

### Git clone the release

```bash
git clone git@github.com:pokusio/try-fastapi.git
cd ./try-fastapi/
git checkout 0.0.1
```




### Install `pipx`

```bash
# First upgrade pip
python -m pip install --upgrade pip
# ---
# Install pipx
python -m pip install --user pipx
python -m pipx ensurepath
# # ---
# # when I want to upgrade pipx after pip :
# python -m pip install --user --upgrade pipx
```



### Install `CookieCutter`, `Poetry`

```bash
pipx install -y cookiecutter
# ---
# Install Poetry
curl -LO https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py && python install-poetry.py

#  Git bash for Windows only:
ls -alh ${HOME}/AppData/Roaming/Python/Scripts/poetry

cat <<EOF >./.addon.windows.git.bashrc
export PATH="\${HOME}/AppData/Roaming/Python/Scripts:\$PATH"
EOF

echo "# -------" | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
echo "# - Poetry" | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
export PATH="${HOME}/AppData/Roaming/Python/Scripts:$PATH"
poetry --version

```

### Run locally

```bash
poetry install
poetry update
poetry shell
poetry run pokusapi
```

### Query the REST API !

* In another shell session, you can then query the new Pokus API : 

```bash
curl -H "X-Token: pokus-super-secret-token" -X GET -ivvv http://127.0.0.1:8000/books/?token=jessica | tail -n 1 | jq .

curl -H "X-Token: pokus-super-secret-token" -X GET -ivvv http://127.0.0.1:8000/users/?token=jessica | tail -n 1 | jq .
```
