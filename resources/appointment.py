from flask import Response, request
from database.models import Appointment, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ItemAlreadyExistsError, \
InternalServerError, UpdatingItemError, DeletingItemError, ItemNotExistsError

class AppointmentsApi(Resource):
    def get(self):
        appointment = Appointment.objects().to_json()
        return Response(appointment, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            appointment = Appointment(**body, added_by=user)
            appointment.save()
            id = appointment.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ItemAlreadyExistsError
        except Exception as e:
            raise InternalServerError
