from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField,DateTimeField,SubmitField
from wtforms.validators import Email, DataRequired
from datetime import datetime


class PostForm(FlaskForm):
    title = StringField('Title', id='title', validators=[DataRequired()])
    slug = StringField('Slug',id='slug')
    body = StringField('Body', id='body')
    created = DateTimeField("Date",default=datetime.now())
    
    class Meta:
        CSRFProtect = False
        csrf = False
        SubmitField= False
        
        
class TagForm(FlaskForm):
    body = StringField('Title', id='title', validators=[DataRequired()])