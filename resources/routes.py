from .patient import PatientsApi, PatientApi
from .admin import AdminApi, AdminsApi
from .admin_appointments import AdminAppointmentsApi
from .hospital import HospitalsApi, HospitalApi
from .hospital_information import HospitalsInfoApi
from .appointment import AppointmentsApi, AppointmentApi

from .auth import SignupApi, LoginApi, Confirm_Email
from .admin_auth import SignupAdminApi,LoginAdminApi, Confirm_Admin_Email

from .reset_password import ForgotPassword, ResetPassword, ForgotAdminPassword,ResetAdminPassword



def initialize_routes(api):
    """Mobile application endpoints"""
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(Confirm_Email, '/api/auth/verify')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')

    api.add_resource(HospitalsInfoApi, '/api/hospitalsinfo')

    api.add_resource(PatientsApi, '/api/patients')
    api.add_resource(PatientApi, '/api/patient/<id>')

    api.add_resource(AppointmentsApi, '/api/appointments')
    api.add_resource(AppointmentApi, '/api/appointment/<id>')

    """Admin side endpoints"""
    api.add_resource(SignupAdminApi, '/api/auth/admin/signup')
    api.add_resource(Confirm_Admin_Email, '/api/auth/admin/verify')
    api.add_resource(LoginAdminApi, '/api/auth/admin/login')

    api.add_resource(HospitalsApi, '/api/hospitals')
    api.add_resource(HospitalApi, '/api/hospital/<id>')

    api.add_resource(ForgotAdminPassword, '/api/auth/admin/forgot')
    api.add_resource(ResetAdminPassword, '/api/auth/admin/reset')

    api.add_resource(AdminApi, '/api/admins')
    api.add_resource(AdminsApi, '/api/admin/<id>')

    api.add_resource(AdminAppointmentsApi, '/api/adminappointments')
