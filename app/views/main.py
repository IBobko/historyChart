# app/views/main.py
from flask import render_template_string
from flask import Blueprint
from flask import request
from flask import send_file
from app.services.timeline_service import TimelineService
from flask import render_template

main = Blueprint('main', __name__)




@main.route('/')
def index():
    return render_template('base.html')



@main.route('/greet', methods=['GET', 'POST'])
def greet():
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
def timeline_png(timeline_service: TimelineService):
    buf = timeline_service.generate_timeline()
    return send_file(buf, mimetype='image/png')