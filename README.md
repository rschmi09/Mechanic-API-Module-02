README.md

-------------------------------------
Project Overview
-------------------------------------
Backend Specialization 01 Assignment01

PROJECT GOAL:

Expand upon implemented customer blueprint with Marshmallow schemas and completed all CRUD routes in and Application Factory Pattern by adding blueprints and routes for the remaining models: 'mechanic' and 'service_ticket'.

Test each route as it is created in Postman inside a collection. Once project is complete export collection and add to project.


-------------------------------------
Project Installations
-------------------------------------
(also in requirements.txt)

blinker==1.9.0
click==8.3.3
colorama==0.4.6
Flask==3.1.3
flask-marshmallow==1.5.0
Flask-SQLAlchemy==3.1.1
greenlet==3.5.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
marshmallow==4.3.0
marshmallow-sqlalchemy==1.5.0
mysql-connector-python==9.7.0
SQLAlchemy==2.0.49
typing_extensions==4.15.0
Werkzeug==3.1.8


-------------------------------------
Project Architecture
-------------------------------------
Mechanic_API
|
|
|_app
|    |_blueprints
|    |    |_customers
|    |    |   |___init__.py
|    |    |   |_routes.py
|    |    |   |_schemas.py
|    |    |_mechanic
|    |    |   |___init__.py
|    |    |   |_routes.py
|    |    |   |_schemas.py  
|    |    |_service_ticket
|    |        |___init__.py
|    |        |_routes.py
|    |        |_schemas.py     
|    |
|    |_ __init__.py
|    |_ extensions.py
|    |_ models.py
|
|_app.py
|_config.py
|_filestructure.txt
|_Mechanic_API.postman_collection.json
|_README.md
|_requirements.txt


-------------------------------------
Project Useage 
-------------------------------------

Create and test routes to populate tables for a 'mechanic shop'.