"""
Does the following:

1. Generates and saves random secret key
2. Removes the taskapp if celery isn't going to be used
3. Removes the .idea directory if PyCharm isn't going to be used
4. Copy files from /docs/ to {{ cookiecutter.project_slug }}/docs/

    TODO: this might have to be moved to a pre_gen_hook

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py
"""
import os
import random
import shutil
import string

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

def get_random_string(length=50):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    punctuation = string.punctuation.replace('"', '').replace("'", '')
    punctuation = punctuation.replace('\\', '')
    if using_sysrandom:
        return ''.join(random.choice(
            string.digits + string.ascii_letters + punctuation
        ) for i in range(length))

    print(
        "Cookiecutter Django couldn't find a secure pseudo-random number generator on your system."
        " Please change change your SECRET_KEY variables in conf/settings/local.py and env.example"
        " manually."
    )
    return "CHANGEME!!"

def set_secret_key(setting_file_location):
    # Open locals.py
    with open(setting_file_location) as f:
        file_ = f.read()

    # Generate a SECRET_KEY that matches the Django standard
    SECRET_KEY = get_random_string()

    # Replace "CHANGEME!!!" with SECRET_KEY
    file_ = file_.replace('CHANGEME!!!', SECRET_KEY, 1)

    # Write the results to the locals.py module
    with open(setting_file_location, 'w') as f:
        f.write(file_)

def make_secret_key(project_directory):
    """Generates and saves random secret key"""
    # Determine the local_setting_file_location
    local_setting = os.path.join(
        project_directory,
        'config/settings/local.py'
    )

    # local.py settings file
    set_secret_key(local_setting)

    env_file = os.path.join(
        project_directory,
        'env.example'
    )

    # env.example file
    set_secret_key(env_file)

def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def remove_heroku_files():
    """
    Removes files needed for heroku if it isn't going to be used
    """
    filenames = ["Procfile", "runtime.txt"]
    for filename in ["Procfile", "runtime.txt"]:
        file_name = os.path.join(PROJECT_DIRECTORY, filename)
        remove_file(file_name)

def remove_client_dir():
    """
    Removes the client directory used by webpack
    """
    client_dir_location = os.path.join(
        PROJECT_DIRECTORY,
        'client'
    )
    shutil.rmtree(client_dir_location)


def remove_webpack_files():
    """
    Removes files needed for grunt if it isn't going to be used
    """
    for filename in ["webpack.config.js"]:
        os.remove(os.path.join(
            PROJECT_DIRECTORY, filename
        ))

def remove_packageJSON_file():
    """
    Removes files needed for grunt if it isn't going to be used
    """
    for filename in ["package.json"]:
        os.remove(os.path.join(
            PROJECT_DIRECTORY, filename
        ))

def remove_copying_files():
    """
    Removes files needed for the GPLv3 licence if it isn't going to be used
    """
    for filename in ["COPYING"]:
        os.remove(os.path.join(
            PROJECT_DIRECTORY, filename
        ))

def remove_open_source_files():
    """
    Removes files conventional to opensource projects only.
    """
    for filename in ["CONTRIBUTORS.txt"]:
        os.remove(os.path.join(
            PROJECT_DIRECTORY, filename
        ))

# 1. Generates and saves random secret key
make_secret_key(PROJECT_DIRECTORY)

# 4. Removes all heroku files if it isn't going to be used
if '{{ cookiecutter.use_heroku }}'.lower() != 'y':
    remove_heroku_files()

# 11. Removes files needed for the GPLv3 licence if it isn't going to be used.
if '{{ cookiecutter.open_source_license}}' != 'GPLv3':
    remove_copying_files()

# 11. Removes webpack files
if '{{ cookiecutter.use_webpack}}' == 'n':
    remove_webpack_files()
    remove_packageJSON_file()
    remove_client_dir()

# 13. Remove files conventional to opensource projects only.
if '{{ cookiecutter.open_source_license }}' == 'Not open source':
    remove_open_source_files()
