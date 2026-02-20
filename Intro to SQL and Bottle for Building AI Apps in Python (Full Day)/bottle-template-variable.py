from bottle import run, route, template

@route('/')
def index():
    class_name = 'Intro to Stuff'
    roster = ['bob', 
            'sue',
            '<a href="http://cnn.com">tim</a>',
            'pam']
    return template('variables', kids=roster, title=class_name,message='this is a message')

run(host='127.0.0.1', port='8080')