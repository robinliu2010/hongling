from flask import Blueprint,render_template
from hongling.models import Course
from hongling.forms import LoginForm,RegisterForm
from flask import flash
from flask import redirect,url_for
from flask_login import login_user,logout_user,login_required
from hongling.models import User

front=Blueprint('front',__name__)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录','success')
    return redirect(url_for('.index'))

@front.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        login_user(user,form.remember_me.data)
        return redirect(url_for('.index'))

    return render_template('login.html',form=form)

@front.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！','success')
        return redirect(url_for('.login'))
    return render_template('register.html',form=form)

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

