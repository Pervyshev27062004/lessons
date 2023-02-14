from lesson_13db.models import User


def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user


def get_users(session):
    users = session.query(User).all()
    return [u.as_dict() for u in users]