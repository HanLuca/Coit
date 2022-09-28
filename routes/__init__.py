from flask import Flask
from . import _Manage, A_Login, A_Profile, A_Register

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.register_blueprint(_Manage.Manage)
app.register_blueprint(A_Login.Account_Login)
app.register_blueprint(A_Profile.Account_Profile)
app.register_blueprint(A_Register.Account_Register)