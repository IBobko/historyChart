# app/views/main.py
from flask import render_template_string
from flask import Blueprint
from flask import request
from flask import send_file
from app.services.timeline_service import TimelineService
from injector import inject
from flask import url_for
from flask import render_template
from flask import current_app
from dependency_injector.wiring import inject, Provide
from app.container import Container


main = Blueprint('main', __name__)




@inject
@main.route('/')
def index(my_service: TimelineService = Provide[Container.my_service]):

    return render_template('base.html')



@main.route('/greet', methods=['GET', 'POST'])
def greet():
    print(url_for('static', filename='css/dist/styles.css'))
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}!'
    return render_template_string('''
        <img src="/timeline" alt="Timeline Image">
        <form method="post">
            Your name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    ''')

@main.route('/timeline')
@inject
def timeline_png(timeline_service: TimelineService = Provide[Container.my_service]):
    buf = timeline_service.generate_timeline()
    return send_file(buf, mimetype='image/png')