from flask import Flask
app = Flask(__name__)

@app.route('/admin')
def hello_world():
   return 'tomy'

if __name__ == '__main__':
   app.run()