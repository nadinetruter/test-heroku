from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Patient(db.Document):
    name = db.StringField(required=True)
    surname = db.StringField(required=True)
    gender = db.StringField(required= True)
    id_number = db.StringField(required = True)
    address = db.StringField(required=True)
    city = db.StringField(required=True)
    country = db.StringField(required=True)
    postal_code = db.StringField(required=True)
    phone_number =db.StringField(required=True)
    primary = db.BooleanField(required = False)
    added_by = db.ReferenceField('User')



class Hospital(db.Document):
    hospital_name = db.StringField(required=True)
    hospital_address = db.StringField(required=True)
    added_by = db.ReferenceField('User')

class Appointment(db.Document):
    patient_selected = db.ReferenceField('Patient')
    hospital_selected = db.ReferenceField('Hospital')
    appointment_date = db.DateTimeField(format="%Y-%m-%dT%H:%M", required = True, unique = True)
    #appointment_time = db.DateTimeField(format="%H:%M", required = True, unique = True)
    ward_type = db.StringField(required = True)
    reason_for_visit = db.StringField(required = True)
    added_by = db.ReferenceField('User')




class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    patients = db.ListField(db.ReferenceField('Patient', reverse_delete_rule=db.PULL))
    hospitals = db.ListField(db.ReferenceField('Hospital', reverse_delete_rule=db.PULL))


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Patient, 'added_by', db.CASCADE)
User.register_delete_rule(Hospital, 'added_by', db.CASCADE)
User.register_delete_rule(Appointment, 'added_by', db.CASCADE)

#admin side models
class Admin(db.Document):
    name = db.StringField(required=True)
    surname = db.StringField(required=True)
    gender = db.StringField(required= False)
    id_number = db.StringField(required = False)
    address = db.StringField(required=False)
    city = db.StringField(required=False)
    country = db.StringField(required=False)
    postal_code = db.StringField(required=False)
    phone_number =db.StringField(required=False)
    primary = db.BooleanField(required = False)
    added_by = db.ReferenceField('AdminSignUp')

class AdminSignUp(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    admin = db.ListField(db.ReferenceField('Admin', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


#if a user is deleted then the movie created by the user is also deleted.
AdminSignUp.register_delete_rule(Admin, 'added_by', db.CASCADE)
