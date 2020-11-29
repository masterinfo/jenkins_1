from flask import Flask

app = Flask(__name__)

#bonjour
@app.route('/')
def hello_world():
    return 'Hello World! vive github'


@app.route('/wil')
def hello_world2():
    return 'Hello World! vive github de wilfrid'





if __name__ == '__main__':
    app.run()
