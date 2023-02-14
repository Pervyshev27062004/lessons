import logging

from flask import Flask, request
from sqlalchemy import create_engine

from lesson_13db.services import get_users, create_user
from lesson_13db.utils import create_tables

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def users_get():
    return get_users(app.session)


@app.route("/", methods=["POST"])
def users_post():
    user = create_user(app.session, request.form.get("email"), request.form.get("password"))
    return {"user_id": user.id}


if __name__ == "__main__":
    engine = create_engine("postgresql://pervyshev:pervyshev@localhost/pervyshev")
    app.session = create_tables(engine)
    app.run()