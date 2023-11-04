# app/views/main.py
from flask import Blueprint
from flask import request

main = Blueprint('main', __name__)

@main.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}!'
    return '''
        <form method="post">
            Your name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''
