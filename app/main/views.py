from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required
from flask_login import login_required, current_user
from . import main
from ..auth.forms import LoginForm
from ..models import Newblog, Comment
from .forms import BlogForm, CommentsForm


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("Profile/profile.html", user = user)



@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def comment(id):
    comments = Comment.query.filter_by(Newblog_id=id).all()
    return render_template('comments.html', comments=comments)



@main.route('/post/comments/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentsForm()

    if form.validate_on_submit():
        new_comment = Comment(Newblog_id=id, comments=form.comments.data)

        db.session.add(new_comment)
        db.session.commit()
        return redirect("/")

    title = ' comment'
    return render_template('new_comment.html',title = title, comment_form=form)



@main.route('/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    posts = Newblog.query.all()

    if form.validate_on_submit():
        title = form.title.data
        New_Post = form.content.data
        new_blog = Newblog(actual_blog=New_Post, title=title)
        new_blog.save_Newbolg()
        return redirect("/")

    return render_template('blogs.html', Newblog_form = form, posts=posts)



@main.route("/sports")
def sports():
    return render_template('sports.html', title = 'sports')

@main.route("/contactme")
def contactme():
    return render_template('contactme.html', title = 'contactme')

@main.route("/education")
def education():
    return render_template('education.html', title = 'education')

@main.route("/interests")
def interests():
    return render_template('interests.html', title = 'interests')

@main.route("/vision")
def vision():
    return render_template('vision.html', title = 'vision')

