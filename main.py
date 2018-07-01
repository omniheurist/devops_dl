from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_devops():
  return 'This is DEVOPS_DL on Azure CD/CI v1'

if __name__ == '__main__':
  app.run()
