from flask import Blueprint, render_template, request, flash
from Core.database import db
from Forms.forms import LogonForm
from Core import models

users_bp = Blueprint('users', __name__, template_folder='templates', static_folder='static')


@users_bp.route('/recovery')
def recovery():
    """
    Renders the 'index.html' template for the '/recovery' route.

    :return: The rendered 'index.html' template.
    """

    users = models.Users.query.all()

    return render_template('recovery.html', users=users)


@users_bp.route('/users/register', methods=['GET', 'POST'])
def register():
    form = LogonForm(request.form)

    if request.method == 'GET':
        return render_template('logon.html', form=form)

    elif request.method == 'POST':

        from Forms.forms import validate_name, validate_email

        val_name = validate_name(form.name)
        val_email = validate_email(form.email)

        if form.validate_on_submit() and val_name and val_email:
            user = models.Users(
                name=request.form['name'], email=request.form['email'],
                password=request.form['password']
            )

            db.session.add(user)
            db.session.commit()

        elif not val_name:
            flash('Nickname already in use')

        elif not val_email:
            flash('Email already in use')

        return render_template('logon.html', form=form)



@users_bp.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        users = models.Users.query.all()
        user_exists = request.form.get('email') in [user.email for user in users]
        validation = request.form.get('password') in [user.password for user in users]

        if user_exists and validation:
            return render_template('homepage.html')

        elif not validation:
            flash('Incorrect password', 'error')
            return render_template('login.html', email=request.form['email'])

        elif not user_exists:
            flash('User does not exist', 'error')
            return render_template('login.html')
