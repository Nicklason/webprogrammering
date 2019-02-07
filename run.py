#from dotenv import dotenv_values as dotenv

from app import app

#app.env = dotenv.get('ENV', 'development')
app.env = 'development'
if __name__ == '__main__':
    app.run(debug=True)#dotenv().get('DEBUG', True))