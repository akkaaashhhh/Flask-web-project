from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,user_to_check): #validate_username is used because validate is used by FlaskForm to check through the existing fields
        user = User.query.filter_by(username=user_to_check.data).first() #.data is important, else interface error occurs
        if user:
            raise ValidationError('username already exists!')


    username = StringField(label='username ', validators=[Length(min=2,max=15),DataRequired()])
    password1 = PasswordField(label='password ',validators=[Length(min=5),DataRequired()])
    password2 = PasswordField(label='Confirm password ',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='username ', validators=[DataRequired()])
    password = PasswordField(label='password ',validators=[DataRequired()])
    submit=SubmitField(label='Sign In')

class addtocartForm(FlaskForm):
    submit=SubmitField(label='Buy Item')

class SellItemForm(FlaskForm):
    submit=SubmitField(label='Sell Item!')
     