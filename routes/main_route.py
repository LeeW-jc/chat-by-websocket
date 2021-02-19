from flask import (
    redirect,
    request,
    session,
    render_template,
    url_for,
    Blueprint,
)

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            return redirect('/')
        session['user_name'] = name
        return redirect(url_for('.chat'))
    return render_template('login.html')


@main.route('/chat')
def chat():
    name = session.get('user_name', None)
    if not name:
        return redirect('/')
    return render_template('chat.html')



