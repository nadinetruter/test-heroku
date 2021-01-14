# ByteMe-backend

Under construction

# Backend Flask-Restful Api Setup and Details

FRAMEWORK: Python Flask framework

LANGUAGE: Python

ENV: export ENV_FILE_LOCATION=./.env

#CRUD = CREATE,READ,UPDATE,DELETE

Api-Admin includes:
1. Admin personal information [CRUD]
2. Signup and Login Api [POST]
3. Authorization and Authentication [POST]
4. Password Reset [POST]
5. Admin read and delete User appointment [GET,DELETE] 

Api-User includes:
1. Patient personal information [CRUD] 
3. Appointment information [CRUD]
4. Authorization and Authentication [POST]
5. Password Reset [POST]

IN ORDER TO RUN ON LOCAL SERVER:
1. open git or cmd
2. activate virtual env
3. run export ENV_FILE_LOCATIONN=./.env
4. run python run.py


API TESTING DONE on POSTMAN:
1. download postman
2. run app
3. start testing using localhost

LOCALHOST: 127.0.0.1:5000

TESTING OUT PASSWORD RESET:
1. open cmd or git
2. run python -m smtpd -n -c DebuggingServer localhost:1025
3. open app cmd/git command line
4. run app.py
5. run password reset test on postman

DATABASE: MONGODB, Mongo compass



