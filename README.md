# Let's Try FastAPI


## Build a python modern project

I finally first chose to run from a cookiecutter generated project:


* for SetupTools classifiers values reference : 
  * https://pypi.org/classifiers/  
  * and important for scripting : https://pypi.org/pypi?%3Aaction=list_classifiers
* https://python.plainenglish.io/13-python-tools-every-developer-should-know-4ae1218ff60b
* 

* For Coockie Cutter references : 
  * I used: https://github.com/cjolowicz/cookiecutter-hypermodern-python
  * even better : https://cookiecutter-hypermodern-python.readthedocs.io/en/2022.6.3.post1/guide.html
  * I learned how to generate silently from cookitecutter cli : 
    * https://stackoverflow.com/questions/60458434/cookie-cutter-whats-the-easiest-way-to-specify-variables-for-the-prompts
    * https://cookiecutter.readthedocs.io/en/1.7.0/advanced/user_config.html
    * https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html#user-config


### 0. Requirements 

* Python version : 

```bash
Utilisateur@Utilisateur-PC MINGW64 ~/try-fastapi (develop)
$ python --version
Python 3.10.5

```

### CoockieCutter

* First install `pipx`

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


* Then install `pyenv` to manage python versions : 

```bash

curl https://pyenv.run | bash



cat <<EOF >./.addon.linux.git.bashrc
export PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF

# git bash for windows Only :
ls -alh /c/Users/$(whoami)/.pyenv/libexec/pyenv
ls -alh ${HOME}/.pyenv/bin/pyenv
cat /c/Users/$(whoami)/.pyenv/bin/pyenv
cat ${HOME}/.pyenv/bin/pyenv

echo "\${HOME}/.pyenv/libexec/pyenv" | tee ${HOME}/.pyenv/bin/pyenv

/c/Users/$(whoami)/.pyenv/libexec/pyenv --version
${HOME}/.pyenv/bin/pyenv --version


cat <<EOF >./.addon.windows.git.bashrc
export PATH="\$HOME/.pyenv/libexec:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF

echo "# -------" | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
echo "# - PyEnv" | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
# cat ./.addon.linux.git.bashrc | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
cat ./.addon.windows.git.bashrc | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile

source ~/.profile

pyenv --version

python --version
pyenv install 3.10.2
# $ pyenv install 3.10.2
# Downloading Python-3.10.2.tar.gz...
# -> https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz
pyenv install 3.10.5

# ---
# make these Python versions accessible in the project directory, using the following command:
pyenv local 3.10.2 3.10.5
# !!! The desired python versions do HAVE to be installed by pyenv, and then local, otherwise : 
# $ pyenv install 3.10.2
# Downloading Python-3.10.2.tar.gz...
# -> https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz
# 
# Utilisateur@Utilisateur-PC MINGW64 ~/try-fastapi/pokusapi (develop)
# $ pyenv local 3.10.2 3.10.5
# pyenv: version `3.10.2' not installed
# 
# Utilisateur@Utilisateur-PC MINGW64 ~/try-fastapi/pokusapi (develop)
# $ pyenv local 3.10.5
# pyenv: version `3.10.5' not installed
```

* Install Cookie Cutter, Poetry
```bash
pipx install -y cookiecutter
# ---
# Install Poetry
curl -LO https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py && python install-poetry.py

# git bash for Windows only
ls -alh ${HOME}/AppData/Roaming/Python/Scripts/poetry

cat <<EOF >./.addon.windows.git.bashrc
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
EOF

cat <<EOF >./.addon.windows.git.bashrc
export PATH="\${HOME}/AppData/Roaming/Python/Scripts:\$PATH"
EOF

echo "# -------" | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
echo "# - Poetry" | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
# cat ./.addon.linux.git.bashrc | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile
cat ./.addon.windows.git.bashrc | tee -a ~/.bashrc | tee -a ~/.bash_profile | tee -a ~/.profile

# source ~/.profile
export PATH="${HOME}/AppData/Roaming/Python/Scripts:$PATH"
poetry --version





pipx install nox
pipx inject nox nox-poetry

pipx upgrade cookiecutter
pipx upgrade --include-injected nox
poetry self update
```


* generate the cookie cutter project : 
```bash
# https://github.com/cjolowicz/cookiecutter-hypermodern-python
# even better : https://cookiecutter-hypermodern-python.readthedocs.io/en/2022.6.3.post1/guide.html
# https://stackoverflow.com/questions/60458434/cookie-cutter-whats-the-easiest-way-to-specify-variables-for-the-prompts
# ---
# works great, automatically generates my project from the cookie cutter
cat <<EOF >./.cookiecutterrc
default_context:
    full_name: "${PROJECT_NAME}"
    email: "jblasselle@pokusio.io"
    github_username: "Jean-Baptiste-Lasselle"
    project_name: "${PROJECT_NAME}"
    project_slug: "Pokus FastAPI"
    project_short_description: "Let's try with FastAPI!"
    pypi_username: "jblasselle"
    version: 0.0.1-alpha
    use_pytest: y
    use_pypi_deployment_with_travis: y
    add_pyup_badge: y
    command_line_interface: "Click"
    create_author_file: "y"
    open_source_license: "MIT license"

EOF
cat .cookiecutterrc | tee ~/.cookiecutterrc
cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout=2022.6.3 --no-input --config-file ./.cookiecutterrc


cd ${PROJECT_NAME}

poetry update
poetry install




# then you can run it by : (see [tool.poetry.scripts] in pyproject.toml)
poetry run pokusapi

```
* I get such an output : 

```bash
Utilisateur@Utilisateur-PC MINGW64 ~/try-fastapi/PokusAPI (develop)
$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: pokusapi (0.0.1-alpha)

Utilisateur@Utilisateur-PC MINGW64 ~/try-fastapi/PokusAPI (develop)
$ poetry run pokusapi
What's the best API ? Pokus Of Course !
What's the best API ? Pokus, period.
```

* now for `FastAPI`, I follow https://realpython.com/fastapi-python-web-apis/ :

```bash
# python -m pip install fastapi uvicorn[standard]

poetry add fastapi  uvicorn[standard]

# ---
# Let's continue with  https://medium.com/@caetanoog/start-your-first-fastapi-server-with-poetry-in-10-minutes-fef90e9604d9


```
* After that, that's how I could run the fastapi server (after activating) : 

```bash
# ---
#  Its still same command, I integrated it :
#   - using the [tool.poetry.scripts] in [pyproject.toml]
#   - and using https://medium.com/@caetanoog/start-your-first-fastapi-server-with-poetry-in-10-minutes-fef90e9604d9
poetry run pokusapi
# --- 
# and then : 
#   curl -ivvv http://127.0.0.1:8000/books/tomsawyer
```

* Oh I found :
  * this cookie cutter for poery fastapi project : https://github.com/max-pfeiffer/uvicorn-poetry-fastapi-project-template
  * ohhh and an official FastAPI cookiecutter : https://github.com/tiangolo/full-stack-fastapi-postgresql

* ok next steps : https://fastapi.tiangolo.com/tutorial/bigger-applications/
* Now, to organize better the code, here is what i did : 
  * I found a good example fastai poetry example app : 
    * https://github.com/nsidnev/fastapi-realworld-example-app
    * for that app : 
      * the entrypoint is is https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/app/main.py
      * the pyproject.toml has got no script definition to run the app using `poetry run` 
      * that project has a very good structure : i want to omake a cookie cutter from it, and then i will try to build a terraformable REST API
      
  * OKAYYYY FastAI is really interesting : IT NATIVELY SUPPORTS OAUTH2 SCOPES : 
    * https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
    * and it apparently is the next generation fter `Django` and after `Flask`
    * I want to try that : 
      * a very, very simple rest api, for a cloud, with only 2 resources types,
      * and there is Oauth2 OIDC support with scopes
      * I deploy my REST API, with keycloak, and i setup OIDC client
      * then i must check how can my terraform provider authenticate against my REST API (terraform authentication OIDC)
      * I need to complete first https://fastapi.tiangolo.com/tutorial/bigger-applications/




### SetupTools

#### 1. SetupTools: Install Setup Tools (changed for a cookie cutter to setup project)

```bash
python -m pip install --upgrade pip
pip install setuptools
```

#### 2. Setup Tools : Setting up `setup.py` 


```bash
export PROJECT_NAME="pokusapi"
cat <<EOF >./setup.py
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "${PROJECT_NAME}",
    version = "0.0.1",
    author = "Andrew Carter",
    author_email = "jblasselle.pokusio@gmail.com",
    description = ("An demonstration of how to develop, document, and publish, a REST API with FastAPI"),
    license = "GNU GPLv3 Affero",
    keywords = "A example FastAPI project, with setuptools",
    url = "http://packages.python.org/${PROJECT_NAME}",
    packages=['${PROJECT_NAME}', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU GPLv3 Affero License",
    ],
)
EOF
# 
#        "Topic :: Other/Nonlisted Topic",


cat <<EOF >./.pywh.template.pypirc
[pypirc]
servers = pypi
[server-login]
username:your_secret_username
password:your_secret_password
EOF
cat <<EOF >./.public.template.pypirc
[pypirc]
servers = pypi
[server-login]
username:your_secret_username
password:your_secret_password
EOF



pip uninstall setuptools
```



## ANNEX: Installing a private python package repository

* https://warehouse.pypa.io/development/getting-started.html#detailed-installation-instructions

* how to check a network port is used or not : 

```bash
sudo lsof -i:6443 | grep LISTEN
```

> _**Required by elastic search :**_ 
> 
> On Linux systems, persistent limits can be set for a particular user by editing the `/etc/security/limits.conf` file. To set the maximum number of open files for the elasticsearch user to 65,535, add the following line to the limits.conf file:
> 

```ini
elasticsearch  -  nofile  65535
```

* Script : 

```bash
export PYWH_INSTALL_HOME=~/.pywh/.installation/
export PYWH_DESIRED_VERSION="main"
mkdir -p ${PYWH_INSTALL_HOME}
# ---
# First Elasticsearch specific Docker host setup 
# - 
# https://www.elastic.co/guide/en/elasticsearch/reference/master/setting-system-settings.html
# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/file-descriptors.html
# 
sudo -i
# as root only, does not work with sudo : 
ulimit -n 65535
exit
# ---
# now 
sudo mkdir -p /etc/security/
# ---
# For all users '*', instead of just the elasticsearch user : 

echo "# ----" | sudo tee -a /etc/security/limits.conf
echo "# - to run elasticsearch in a docker-compose in [${PYWH_INSTALL_HOME}] " | sudo tee -a /etc/security/limits.conf
echo "*  -  nofile  65535" | sudo tee -a /etc/security/limits.conf

# ---
# Also : 
sudo sysctl -w vm.max_map_count=262144

# ---
# permanently by modifying the vm.max_map_count setting in your /etc/sysctl.conf

echo "# ----" | sudo tee -a /etc/sysctl.conf
echo "# - to run elasticsearch in a docker-compose in [${PYWH_INSTALL_HOME}] " | sudo tee -a /etc/sysctl.conf
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
# ---
# 

# ---
#  We need make for the warehouse build from source
sudo apt-get install -y build-essential


git clone https://github.com/pypi/warehouse/blob/main/docker-compose.yml ${PYWH_INSTALL_HOME}

cd ${PYWH_INSTALL_HOME}

git checkout ${PYWH_DESIRED_VERSION}

# --- warehouse server portnumber then
export WEB_HOST=8083
export PYWH_POKUS_HOST="pywh.pokus.io"
# ---
# build from source first
make build
# HERE I STOPPED : 
#  >> the build was supposed to work, but it did not: yet the build is inside a docker image.
#  >> that's why i decided : 
#      + to first just create an account on pypi.org
#      + then i will try a simple artifactory docker compose, and use artifactory as python package repository.
 
make initdb

# make serve
docker-compose config

echo " Go visit http://${PYWH_POKUS_HOST}:${WEB_HOST}/account/login/ "

docker-compose up -d # ./docker-compose.yml


```

## ANNEX: References 

* About python Setup tools project : 
  * https://pythonhosted.org/${PROJECT_NAME}/setuptools.html
  * 
* About FastAPI : 
  * https://github.com/tiangolo/fastapi
  * https://realpython.com/fastapi-python-web-apis/
* About private self hosted Python Package repositories :
  * https://github.com/vinta/awesome-python#package-repositories
  * by far this is the most github starred : https://github.com/pypi/warehouse