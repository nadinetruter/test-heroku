from flask import Response, request, jsonify
from database.models import Patient, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ItemAlreadyExistsError, \
InternalServerError, UpdatingItemError, DeletingItemError, ItemNotExistsError

class PatientsApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()

        patients = User.objects.get(id=user_id).patients

        return jsonify(patients)

        return Response(patients, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            patient = Patient(**body, added_by=user)
            patient.save()
            user.update(push__patients=patient)
            user.save()
            id = patient.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ItemAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class PatientApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            patient = Patient.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Patient.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingItemError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            patient = Patient.objects.get(id=id, added_by=user_id)
            patient.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingItemError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            patients = Patient.objects.get(id=id).to_json()
            return Response(patients, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ItemNotExistsError
        except Exception:
             raise InternalServerError
