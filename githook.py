from flask import Flask
from flask import request

import simplejson

import sys
from subprocess import CalledProcessError, check_output

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
        post_data = simplejson.loads(request.form['payload'])

        ''' Execute deployment script '''
        try:
            #app.logger.debug('Running Script')
            output = check_output(['bash', '/opt/git_hook/deploy_website.sh'])
            #app.logger.debug(output)

        except CalledProcessError as e:
            app.logger.error('[PROCESS_ERROR]: {}'.format(e))

        except:
            app.logger.error('[OS_ERROR] {}'.format(sys.exc_info()[0]))

        return 'Website Deployed'
    else:
        return 'GET request not supported'


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80, debug=True)
    app.run()
