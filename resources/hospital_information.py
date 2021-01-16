from flask import Response, request
from database.models import Hospital
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

class HospitalsInfoApi(Resource):
    def get(self):
        hospital = Hospital.objects().to_json()
        return Response(hospital, mimetype="application/json", status=200)
