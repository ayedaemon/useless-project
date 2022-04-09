from flask import Blueprint, render_template, request



############################
#
#   AUTH Module views
#
#############################

mod_auth = Blueprint('mod_auth', __name__, template_folder='templates', static_folder='static')



@mod_auth.route('/register', methods=['GET'])
def register():
    response = {}
    if request.method == 'GET':
        return render_template('register.html', title="Register", data=response)
    elif request.method == 'POST':
        print(dir(request))
        return 'SAVED'
        


@mod_auth.route('/login', methods=['GET'])
def login():
    response = {}
    response['msg'] = 'Site under construction'
    response['list_items'] = [
        {'title' : 'One'},
        {'title' : 'Two'},
        {'title' : 'Three'}
    ]

    return render_template('login.html', title="Login", data=response)



