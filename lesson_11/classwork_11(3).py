import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("database1.sqbpro") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
       )
       session.commit()
def delete_user(firstname: str):
   with sqlite3.connect("my_database.sqlite") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           DELETE FROM user
           WHERE firstname = ?;
           """,
           (firstname,),
       )
       session.commit()
def select_user(id: int):
   with sqlite3.connect("database1.sqbpro") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM homework_11(try1)
           WHERE id = ?;
           """,
           (id,)
       )
       session.commit()
       return cursor.fetchone()


if __name__ == "__main__":
    select_user(id)