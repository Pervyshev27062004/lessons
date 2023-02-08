from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
import logging
from lesson_13db.utils import create_tables, create_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_USER = "pervyshev"
DB_PASSWORD = "pervyshev"
DB_NAME = "pervyshev"
DB_ECHO = True

if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_tables(engine)

    menu = """
    1. Создать пользователя
    2. Найти пользователя
    3. Выйти
    """



    while True:
        logger.info(menu)
        choice = input("Выберите функцию: ")

        if choice == "1":
            email = input("Введите почту: ")
            password = input("Введите пароль: ")
            user = create_user(session, email, password)
            logger.info(f"User #{user.id} is created")

        elif choice == "2":
            email = input("Введите почту: ")


        elif choice == "3":
            exit()
        ###select * from "user";




