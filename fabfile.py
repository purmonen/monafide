from fabric.api import *
from fabric.contrib.files import exists

env.hosts = ["54.76.172.54"]
env.user = "ubuntu"
env.key_filename = "../monafide.pem"

def deploy():
    local("git push")
    directory = "monafide"
    if exists(directory):
        with cd(directory):
            run("git pull")
    else:
        run("git clone https://github.com/purmonen/monafide " + directory)
