import sys
import json
from flask import Response, request, jsonify
from database.models import Appointment, User, Patient
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ItemAlreadyExistsError, \
InternalServerError, UpdatingItemError, DeletingItemError, ItemNotExistsError

class AppointmentsApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()

        patients = User.objects.get(id=user_id).patients
        data = []

        for p in patients:
            ap = Appointment.objects.get(**{ "patient_selected" : p["id_number"] })
            if ap:
                data.append(ap)


        return jsonify(data)
        # return Response(data, mimetype="application/json", status=200)

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

class AppointmentApi(Resource):

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            appointment = Appointment.objects.get(id=id, added_by=user_id)
            appointment.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingItemError
        except Exception:
            raise InternalServerError

    @jwt_required
    def get(self, id):
        try:
            user_id = get_jwt_identity()
            appointments = Appointment.objects.get(id=id, added_by=user_id).to_json()
            return Response(appointments, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ItemNotExistsError
        except Exception:
            raise InternalServerError
