from flask import Response, request
from database.models import Hospital, AdminSignUp
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ItemAlreadyExistsError, \
InternalServerError, UpdatingItemError, DeletingItemError, ItemNotExistsError

class HospitalsApi(Resource):
    def get(self):
        hospital = Hospital.objects().to_json()
        return Response(hospital, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = AdminSignUp.objects.get(id=user_id)
            hospital = Hospital(**body, added_by=user)
            hospital.save()
            user.update(push__hospital=hospital)
            user.save()
            id = hospital.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ItemAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class HospitalApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            hospital = Hospital.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Hospital.objects.get(id=id).update(**body)
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
            hospital = Hospital.objects.get(id=id, added_by=user_id)
            hospital.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingItemError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            hospitals = Hospital.objects.get(id=id).to_json()
            return Response(hospitals, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ItemNotExistsError
        except Exception:
             raise InternalServerError
