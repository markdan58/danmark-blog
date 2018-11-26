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


