import json
from urllib.request import urlopen

from flask import jsonify, render_template, request, url_for, flash, redirect
from flask import jsonify
from flask import jsonify, render_template,send_from_directory


from app import app
from app import hw_views
# from app.forms import forms
from app.models.blog_entries import BlockEntry, PostForm
import datetime
from app import oauth

# from app.forms import forms
# from .hw_forms import RegistrationForm

import bcrypt 


@app.route('/hw10', methods=('GET', 'POST'))
def hw10_microblog():
    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))
        id_ = result.get('id', '')
        validated = True
        validated_dict = dict()
        valid_keys = ['name', 'message', 'email']
    return app.send_static_file('hw10_microblog.html')
