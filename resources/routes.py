from .patient import PatientsApi, PatientApi
from .hospital import HospitalsApi, HospitalApi
from .admin import AdminApi, AdminsApi, AdminAppointmentsApi, AdminAppointmentApi
from .appointment import AppointmentsApi

from .auth import SignupApi, LoginApi
from .admin_auth import SignupAdminApi,LoginAdminApi

from .reset_password import ForgotPassword, ResetPassword, ForgotAdminPassword,ResetAdminPassword



def initialize_routes(api):

    api.add_resource(PatientsApi, '/api/patients')
    api.add_resource(PatientApi, '/api/patient/<id>')

    api.add_resource(HospitalsApi, '/api/hospitals')
    api.add_resource(HospitalApi, '/api/hospital/<id>')

    api.add_resource(AdminApi, '/api/admin')
    api.add_resource(AdminsApi, '/api/admin/<id>')

    api.add_resource(AppointmentsApi, '/api/appointments')
    api.add_resource(AdminAppointmentsApi, '/api/adminappointments/')
    api.add_resource(AdminAppointmentApi, '/api/adminappointment/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(SignupAdminApi, '/api/auth/admin/signup')
    api.add_resource(LoginAdminApi, '/api/auth/admin/login')

    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')

    api.add_resource(ForgotAdminPassword, '/api/auth/admin/forgot')
    api.add_resource(ResetAdminPassword, '/api/auth/admin/reset')
