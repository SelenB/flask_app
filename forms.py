from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms import PasswordField, BooleanField, SubmitField

# create a dropdown list asking user what table they want to see
# either top artists/top tracks/top albums. 
#based on selection, open a new page that shows the table with
#some data visualizations/world.

#databasehtml is the page we will be using.

#we also need to define st

#CHELLLLOOOOOO


# found this class that asks users to login. might be a good starting point for
#users login through spotify.
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


