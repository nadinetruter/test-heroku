from flask import Response, request
from database.models import Appointment
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

class AdminAppointmentsApi(Resource):
    def get(self):
        appointment = Appointment.objects().to_json()
        return Response(appointment, mimetype="application/json", status=200)

class AdminAppointmentApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            appointment = Appointment.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Appointment.objects.get(id=id).update(**body)
            return {"message":"Appointment is completed"}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingItemError
        except Exception:
            raise InternalServerError
