with sq.connect("my_practicesql.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS GPS")
    cur.execute("""
    CREATE TABLE if not exists GPS (
    country VARCHAR,
    city VARCHAR,
    population int  
);
    """)
#######################################################
with sq.connect("my_practicesql.db") as con:
    cur = con.cursor()
    cur.execute(""" SELECT *
    FROM GPS
    WHERE country = "Germany" """)
    result = cur.fetchall()
    print(result)