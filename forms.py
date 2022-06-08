from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of puppy:')
    submit = SubmitField('Add puppy')


class DelForm(FlaskForm):
    id = IntegerField('Id number of puppy to remove:')
    submit = SubmitField('Remove puppy')


class AddOwnerForm(FlaskForm):
    owner_name = StringField('Name of Owner')
    pup_id = IntegerField('Id of puppy:')
    submit = SubmitField('Add Owner')
