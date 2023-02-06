from flask import Flask
import controllers5, models5

app = Flask(__name__)
app.secret_key = 'secret_key'

app.register_blueprint(controllers.app)

if __name__ == '__main__':
    models.init_db()
    app.run(debug=True)


