from sqlalchemy.orm import sessionmaker
from lesson_13db.models import Base, User
def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user
def search_user():
    user = User(email=email)
def get_users_by_product_id(session, product_id: int) -> list:
    session.query(Purchase).filter_by(product_id=product_id)
    user_ids = []
    for purchase in purchases:
        user_ids.append(purchase.user_id)
    return list(set(user_ids))
def get_users_by_product_id(session, product_id: int) -> list:
    return session.query(Purchase).filter_by(product_id=product_id).load_only(Purchase.user_id).distinct()