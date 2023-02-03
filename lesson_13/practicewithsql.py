import sqlite3 as sq


def create_user(country: str, city: str, population: int):
    with sq.connect("my_practicesql.db") as session:
        cur = session.cursor()
        cur.execute(
            """
            INSERT INTO GPS ( country, city, population)
            VALUES (?, ?, ?);
            """,
            (country, city, population),
        )
        session.commit()
def delete_user(population: int):
   with sq.connect("my_practicesql.db") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           DELETE FROM GPS
           WHERE population = ?;
           """,
           (population,),
       )
       session.commit()
def search_punct():
    with sq.connect("my_practicesql.db") as session:
        cursor = session.cursor()
        cursor.execute("""
        SELECT city 
        FROM GPS
        WHERE population >= 400 and population <= 1000
        """
        )


if __name__ == "__main__":

    print(search_punct())
    #create_user("Belarus", "Gomel", 500)
    #delete_user("Gomel")
    #delete_user(400)

