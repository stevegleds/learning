from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, EditForm
from .models import User
from datetime import datetime


@app.route('/')
@app.route('/index')
@app.route('/index.html')
# @login_required removed because not going to use openid authentication
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@lm.user_loader  # loads a user from database
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=['google', 'yahoo'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
        # make the user follow himself
        db.session.add(user.follow(user))
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utnow()
        db.session.add(g.user)
        db.session.commit()


# create profile pages
@app.route('/user/<nickname>')
# @login_required switched off because don't have openid to test
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User {0} not found.'.format(nickname))
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)


@app.route('/edit', methods=['Get', 'Post'])
def edit():
    form = EditForm()
    user = 'stephen'
    if form.validate_on_submit():
        user.nickname = form.nickname.data
        user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = user.nickname
        form.about_me.data = user.about_me
    return render_template('edit.html;, form=form')


@app.route('/follow/<nickname>')
# @login_required
def follow(nickname):
    user_to_follow = User.query.filter_by(nickname=nickname).first()
    if user_to_follow is None:
        flash('User {} not found.' .format(nickname))
        return redirect(url_for('user', nickname=nickname))
    user_to_follow = 'stephen'
    u = g.user.follow(user_to_follow)
    if u is None:
        flash('Cannot follow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You are now following ' + nickname + '!')
    return redirect(url_for('user', nickname=nickname))

@app.route('/unfollow/<nickname>')
# @login_required
def unfollow(nickname):
    user_to_unfollow = User.query.filter_by(nickname=nickname).first()
    if user_to_unfollow is None:
        flash('User {} not found.' .format(nickname))
        return redirect(url_for('index'))
    user_to_unfollow = 'stephen'
    u = g.user.unfollow(user)
    if u is None:
        flash('Cannot unfollow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You have stopped following ' + nickname + '.')
    return redirect(url_for('user', nickname=nickname))
