from database.models import AdminSignUp
from flask_restful import Resource
from flask import Response, request,  render_template
from flask_jwt_extended import create_access_token
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError
from services.mail_service import send_email
# signup api for admin to sign up
# makes sure password is hashed
# sends a unique id number
class SignupAdminApi(Resource):
 def post(self):
     url = request.host_url + 'verify/'
     try:
         body = request.get_json()
         user =  AdminSignUp(**body)
         user.hash_password()
         user.save()
         id = user.id
         #return {'id': str(id)}, 200
         expires = datetime.timedelta(hours=24)
         access_token = create_access_token(str(id), expires_delta=expires)
         return send_email('Login verification',
                           sender='bytecare0@gmail.com',
                           recipients=[user.email],
                           text_body=render_template('auth/login_email.txt',
                                                      url=url + access_token),
                           html_body=render_template('auth/login_email.html',
                                                     url=url + access_token))
     except FieldDoesNotExist:
         raise SchemaValidationError
     except NotUniqueError:
         raise EmailAlreadyExistsError
     except Exception as e:
         raise InternalServerError

class Confirm_Admin_Email(Resource):
    def post(self):
        url = request.host_url + 'verify/'
        try:
            body = request.get_json()
            access_token = body.get('access_token')
            password = body.get('password')

            if not access_token or not password:
                raise SchemaValidationError

            #user_id = decode_token(reset_token)['identity']

            return {'message':'The email is verified!'}
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError

#login api for admin to loginto their accounts
#jwt extended used to create the access token thats valid for 7 days
class LoginAdminApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = AdminSignUp.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
