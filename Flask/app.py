from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "Welcome to hell"

@app.route('/home')
def index():
  return "Index Page"


if __name__ == '__main__':
  app.run(debug=True)