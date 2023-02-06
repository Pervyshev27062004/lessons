import sqlite3 as sq
def create_user(id: int, url: str, product_id: int):
    with sq.connect("shop1.sqlite") as session:
        cursor = session.cursor()
        cursor.execute(
              """
               INSERT INTO product_photo (id, url, product_id)
               VALUES (?, ?, ?);
               """,
               (id, url, product_id),
           )
           session.commit()


with sq.connect("shop1.sqlite") as session:
    cursor = session.cursor()
    session.query(product).filter_by(name="Iphone").update({"name": "Iphone 1"})







