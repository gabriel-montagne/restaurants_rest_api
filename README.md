# THIS IS A DJANGO REST API PROJECT

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
- name: string
- opens_at: datetime
- closes_at: datetime
