from flask_wtf import FlaskForm, csrf
from wtforms import BooleanField, IntegerField, FileField
from wtforms.validators import DataRequired, Optional


class SapulatarFrom(FlaskForm):
    class Meta:
        csrf = False
    alpha_matting = BooleanField('alpha_matting', validators=[Optional()])
    alpha_matting_foreground_threshold = IntegerField('alpha_matting_foreground_threshold', validators=[Optional()])
    alpha_matting_background_threshold = IntegerField('alpha_matting_background_threshold', validators=[Optional()]),
    alpha_matting_erode_structure_size = IntegerField('alpha_matting_erode_structure_size', validators=[Optional()]),
    alpha_matting_base_size = IntegerField('alpha_matting_base_size', validators=[Optional()])
    file = FileField('file', validators=[DataRequired()])
