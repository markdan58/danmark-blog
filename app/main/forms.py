from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from ..models import User
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo
from .. import db




class CommentsForm(FlaskForm):
    comments = TextAreaField('Newblog Comments', validators=[Required()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR BLOG')
    submit = SubmitField('SUBMIT')
