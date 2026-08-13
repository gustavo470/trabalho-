from flask import Flask

from database import db
from routes.aluno_routes import aluno_routes


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smartfit.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

app.register_blueprint(aluno_routes)


with app.app_context():
    db.create_all()


@app.route("/")
def inicio():
    return {
        "mensagem": "API Smart Fit funcionando!"
    }


if __name__ == "__main__":
    app.run(debug=True)