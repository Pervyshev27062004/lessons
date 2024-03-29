from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User, Address, Profile

DB_USER = "pervyshev"
DB_PASSWORD = "pervyshev"
DB_NAME = "pervyshev"
DB_ECHO = True



if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # user = User(email="test@test.com", password="password")
    # session.add(user)
    #
    # session.commit()
    #
    # address = Address(user_id=user.id, city="Minsk", address="Test")
    # session.add(address)
    #
    # profile = Profile(user_id=user.id, phone="+375292999999", age=20)
    # session.add(profile)


    session.commit()

    result = session.query(Profile).filter(Profile.age >= 15)
    for x in result:
        print(x)