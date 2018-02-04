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
- load the environment:
```Shell
$> workon restaurants_api
```
- create a superuser:
```Shell
$> python manage.py createsuperuser
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
