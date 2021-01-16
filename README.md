# Userbase-backend

# STILL CURRENTLY IN DEVELOPMENT

Backend Restful api for the user - side interface.

FRAMEWORK:
- FLASK

LANGUAGE:
-Python

ENV:
- export ENV_FILE_LOCATION=./.env


Api include:
- Patient personal information CRUD
  -Functions:
    GET,UPDATE, DELETE, PUT
- Contact information CRUD
  -Functions:
      GET,UPDATE, DELETE, PUT
- Address information CRUD
  -Functions:
    GET,UPDATE, DELETE, PUT
- Authorization and Authentication POST
- Password Reset POST

# CRUD = CREATE,RETRIEVE,UPDATE,DELETE

API TESTING DONE on POSTMAN:
SETUP POSTMAN
- sign in
- import json file located in POSTMAN TESTING folder
- PS in order to test api on postman, first run run.py to start local server

TESTING OUT PASSWORD RESET:
- open cmd or git 
- insert : python -m smtpd -n -c DebuggingServer localhost:1025

IN ORDER TO RUN ON LOCAL SERVER:
- open git or cmd
- activate viual env
- vitual env name == env
- export ENV_FILE_LOCATION=./.env
- python run.py

LOCALHOST: 127.0.0.1:5000

TESTING OUT PASSWORD RESET:
- open cmd or git 
- insert : python -m smtpd -n -c DebuggingServer localhost:1025


ROUTEs:
- GET,POST PatientsApi, '/api/patients'
- GET,UPDATE,DELETE PatientApi, '/api/patient/<id>'
- GET,POST AddressesApi, '/api/addresses'
- GET,UPDATE,DELETE AddressApi, '/api/addresses/<id>'
- GET,POST ContactsApi, '/api/contacts'
- GET,UPDATE,DELETE ContactApi, '/api/contacts/<id>'

- POST SignupApi, '/api/auth/signup'
- POST LoginApi, '/api/auth/login'

- POST ForgotPassword, '/api/auth/forgot'
- POST ResetPassword, '/api/auth/reset'

DATABASE:
-MONGODB
- Mongo compass

Mongodb user.PNG in folder

