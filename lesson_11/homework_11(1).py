import sqlite3


def create_user(name: str, cost: int, number: int, commentary: str):
    with sqlite3.connect("my_database.sqlite") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (name, cost, number, commentary)
            VALUES (?, ?, ?, ?);
            """,
            (name, cost, number, commentary),
        )
        session.commit()


if __name__ == "__main__":
    create_user("bon", 4, 5, "smth")
