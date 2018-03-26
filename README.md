#Laddr

Connecting people with similar goals, complementary skillsets, and cohesive personalities.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

####Git
Install git from [here](https://git-scm.com/downloads). 

The project will be tracked on our [github](https://github.com/JacobSaudan/Laddr), and you will need to get a feel for how to use it. A good cheat-sheet can be found [here]().

Pulling the code is simple. Navigate to the location you would like to keep the project and `git clone https://github.com/JacobSaudan/Laddr.git`. Enter your user name and password and you will begin the download.

It will be important for good bookkeeping to match branch naming conventions. A good rule of thumb is to name branches `<token>/name`. "\<token>" is a short descriptive noun, while "name" should be indicative of the work being done on the branch. Common tokens are

- feature: for introducing new features in development
- bugfix: for fixing bugs in development
- hotfix: for fixing bugs in production

#### Python
We are using python 3.6. It can be downloaded from python's [homepage](https://www.python.org/downloads/).

#### Python Virtual Environment
Python virtual environment will allow you to isolate project requirements with ease. Follow download and installation instructions [here](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html). You will want to make your environment just above the root project directory so that your file architecture is like so:

```
- Projects
  - laddr_env
  - Laddr
    - Laddr
    - manage.py
    - README.md
    - requirements.txt 

```

Creating an environment is outlined [here](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html#pymote-virtual-environment). Once your virtualenvironment is active, you will want to install the project requirements `pip install -r requirements.txt`. This command of course assumes you are at the root directory for the project.

#### Postgres
Steps for installing postgres can be found online [here](https://www.postgresql.org/download/windows/).
### Installing

Once prerequisites are installed, you will want to clone the repository locally.

```
git clone https://github.com/JacobSaudan/Laddr.git <name>(optional)
```

Next create a postgres user to manage the application.

```
createuser <name>
```

Create a `settings_local.py` file by copying `settings_local.py.default` and fill in the information for postgres. You will need to make and apply django migrations.

```
python manage.py makemigrations
python manage.py migrate
```

All that is left to do is run the development server on django and you will be ready to develop!

```
python manage.py runserver
```
