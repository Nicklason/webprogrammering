from dotenv import dotenv_values as dotenv
from flask import Flask

app = Flask(__name__)

app.env = dotenv().get('ENV', 'development')

@app.route('/')
def index():
    return 'det virker'

if __name__ == "__main__":
    app.run(debug=dotenv().get('DEBUG', True))
