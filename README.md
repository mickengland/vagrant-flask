# vagrant-flask
### Introduction
This is an example flask api to add json to a database and then do a count of users for a given date.

### Ansible

This example assumes that Ansible is running on your host machine.

Install the following roles from Ansible Galaxy:

ansible-galaxy install geerlingguy.repo-epel

ansible-galaxy install wtanaka.pip

ansible-galaxy install andrewrothstein.flask

ansible-galaxy install d4rkstar.mongodb

### Vagrant

vagrant up

vagrant provision

(Forcing the provisioner with vagrant up does not seem to work for some reason)

### Running the flask app

python api.py

### Testing

The bash script test.sh will make a curl request to add a user and then run a get to count the number of users for a given date.




