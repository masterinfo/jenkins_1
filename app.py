from flask import Flask

app = Flask(__name__)

#bonjour
@app.route('/')
def hello_world():
    return 'Hello World! vive github'


@app.route('/git')
def hello_world3():
    return 'Hello World!  qui declenche jenkins depui github'


@app.route('/gpizza45f')
def hello_world45f():
    return 'Hello World!  qui declenche jenkins depui github pizza'


@app.route('/gpizza45')
def hello_world45():
    return 'Hello World!  qui declenche jenkins depui github pizza'



if __name__ == '__main__':
    app.run()
