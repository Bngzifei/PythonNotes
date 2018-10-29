from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'this is index view'


if __name__ == '__main__':
    app.run()
