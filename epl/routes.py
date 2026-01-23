from epl import app

@app.route('/')
def index():
    return {'message': 'Welcome to Flask-EPL!'}

@app.route('/health')
def health():
    return {'status': 'ok'}, 200
