# In the name of Allah

from flask_wtf import FlaskForm
from wtforms import RadioField

class SettingsForm(FlaskForm):
    host = RadioField('Allow requests from unknown hosts',choices=[('1','Allow'),('0','Disallow')])
