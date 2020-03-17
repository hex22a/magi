# MAGI

Backend server for AI experiments running in WEB

## Installation

This project uses [Conda](https://docs.conda.io/) to manage project dependencies.
Also recommended to use [pyenv](https://github.com/pyenv/pyenv) as a Python version manager so you can have multiple concurrent versions of python installed on your machine.
Check out [pyenv-installer](https://github.com/pyenv/pyenv-installer) or install via brew if you're on Mac.

#### Clone this repo and switch current directory

```bash
git clone git@github.com:hex22a/magi.git && cd ./magi
```

#### Install conda (miniconda)

```bash
pyenv install miniconda3-latest
```

#### Create virtual Conda environment

The following command will create `env` folder in your project directory. This folder will contain local Python executable as well as all of the dependencies.

```bash
conda env create --prefix ./envs -f environment.yml
```

Notice that it also installs dependencies listed in [environment.yml](environment.yml)

#### Activate the environment

After creating an environment you need to tell shell to start actually using it.

```bash
conda activate ./envs
```

After running this command you will notice that your command line prompt is now prefixed with a full path to your `env` folder.

For more information visit [Conda Docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Running server

```bash
python ./src/start_server.py
``` 

## Testing

TBD;

## Deployment

TBD;

## Useful commands

TBD;