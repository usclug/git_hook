from flask import Flask
from flask import request

import simplejson

app = Flask(__name__)

@app.route('/')
def index():
    #app.logger.debug(request)    
    return 'Welcome to GitHook!'


'''
This a sample hook
'''
@app.route('/deploy', methods=['GET', 'POST'])
def deploy():
    if request.method == 'POST':
        #app.logger.debug(payload)
        post_data = simplejson.loads(request.form['payload'])
        return 'Deploy Website'
    else:
        return 'GET request not supported'


if __name__ == '__main__':
    #app.debug = True
    #app.host = '0.0.0.0'
    app.run()
