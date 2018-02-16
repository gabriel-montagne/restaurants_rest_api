# DJANGO REST FRAMEWORK API PROJECT

Specifications:

The api responses use json over api:

CRUD operations are implemented on restaurants objects.

Example:
  - GET: /restaurant return list of restaurants
  - GET: /restaurant/{id} return restaurant object
  - POST: /restaurant add a new restaurant
  - PATCH: /restaurant/{id} update the restaurant for spec id
  - DELETE: /restaurant/{id} delete the restaurant for spec id

The restaurants object has the following fields:
- id: integer
- name: string (assumption: there can be no two restaurants with the same name)
- opens_at: datetime
- closes_at: datetime

Permissions(assumption):
  - authenticated users can: read, create, update and delete records
  - not authenticated users can: read and create records

Steps to use the repository:
- make sure you have django, djangoframework, git, vagrant and virtualbox installed:
  - to install django and djangoframework follow the instructions at  http://www.django-rest-framework.org/tutorial/quickstart/
  - to install git follow the instructions at https://gist.github.com/derhuerst/1b15ff4652a867391f03
  - to install vagrant follow the instructions at https://www.vagrantup.com/
  - to install VirtualBox follow the instructions at https://www.virtualbox.org/
- open the console(terminal for OS)
- clone the respository in your workspace:
```Shell
$> git clone  https://github.com/gabriel-montagne/restaurants_rest_api.git
```
- navigate to the project folder:
```Shell
$> cd restaurants_rest_api
```
- start the vagrant VM:
```Shell
$> vagrant up
```
- connect to the VM:
```Shell
$> vagrant ssh
```
- change the directory:
```Shell
$> cd /vagrant/src/restaurants_project
```
- create the environment (only on first run):
```Shell
$> mkvirtualenv restaurants_api
```
- load the environment:
```Shell
$> workon restaurants_api
```
- change the directory:
```Shell
$> cd ../../
```
- install the dependencies:
```Shell
$> pip install -r requirements.txt
```
- check the installed dependencies:
```Shell
$> pip freeze
Django==1.11
djangorestframework==3.6.2
packaging==16.8
pbr==3.1.1
psycopg2==2.7.3.2
pyparsing==2.2.0
pytz==2017.3
six==1.10.0
stevedore==1.28.0
virtualenv==15.1.0
virtualenv-clone==0.2.6
virtualenvwrapper==4.8.2
```
- create a superuser:
```Shell
$> python src/restaurants_project/manage.py createsuperuser
```
- change the directory:
```Shell
$> cd src/restaurants_project
```
- to run the tests type:
```Shell
$> python manage.py test
```
- to run the server type:
```Shell
$> python manage.py runserver 0.0.0.0:8080
```
- open the browser and navigate to: 127.0.0.1:8080/admin/login/
- login using your superuser credentials
- after login navigate to: 127.0.0.1:8080/api/restaurant to see the list and(or) add a new restaurant
- to update/delete a specific item, navigate to 127.0.0.1:8080/api/restaurant/{id}


## Docker
to run the app in docker with PostreSQL persistance layer run:
```
> docker-compose up
```

  Then open the browser and navigate to 127.0.0.1:8000/admin/login

authenticate with:
```
user = admin
password= asdf1234
```