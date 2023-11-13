from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from Core.models import Users

render_kw = {
    '0': {'placeholder': 'Enter your nickname'},
    '1': {'placeholder': 'Enter your email'},
    '2': {'placeholder': 'Enter your password'},
}


class LogonForm(FlaskForm):
    name = StringField(
        'Enter your nickname',
        validators=[DataRequired()],
        render_kw=render_kw['0'])

    email = EmailField(
        'Enter your email',
        validators=[DataRequired(), Email()],
        render_kw=render_kw['1']
    )

    password = PasswordField(
        'Enter your password here', validators=[DataRequired(), Length(min=7)],
        render_kw=render_kw['2']
    )

    submit = SubmitField('submit')


def validate_name(field):

    """
    Validate the name field.

    Parameters:
        field (Field): The name field to be validated.

    Raises:
        ValidationError: If the nickname is already in use.

    Returns:
        None
    """

    if Users.query.filter_by(name=field.data).first() is None:
        pass

    elif Users.query.filter_by(name=field.data).first():
        raise ValidationError('Nickname already in use')


def validate_email(field):

    """
    Validate the email field.

    Parameters:
    - field: The email field to be validated.

    Returns:
    - None

    Raises:
    - ValidationError: If the email is already in use.
    """

    if Users.query.filter_by(email=field.data).first() is None:
        return True

    elif Users.query.filter_by(email=field.data).first():
        raise ValidationError('Email already in use')

    return False


class LoginForm(FlaskForm):
    name_email = StringField("Enter nickname or email", validators=[DataRequired()])
    password = PasswordField("Enter password", validators=[DataRequired()])
    submit = SubmitField("submit")
