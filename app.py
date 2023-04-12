from flask import Flask
from posts import posts
from weather import weather

app = Flask(__name__)

app.register_blueprint(posts,url_prefix='/posts')
app.register_blueprint(weather,url_prefix='/weather')

if __name__ == '__main__':
    app.run(debug=True,port=3000)