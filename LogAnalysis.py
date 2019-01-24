#!/usr/bin/env python
# import library for postgres db
import psycopg2


def main():
    # connect to database identify db by name
    conn = psycopg2.connect("dbname=news")

    # object that will execute results
    cursor = conn.cursor()

    query1 = """
    select articles.title as title, count(log.path) as views
    from articles
    join log on CONCAT('/article/',articles.slug)=log.path
    group by articles.title
    order by views DESC LIMIT 3;
    """

    query2 = """
    select authors.name as authors, count(log.path) as totalsbyauthor
    from articles
    left outer join authors on (authors.id = articles.author)
    left outer join log on concat('/article/',articles.slug)=log.path
    group by authors
    order by totalsbyauthor desc;
    """

    query3 = """
    select date, percent from errorrate where percent >1;
    """
    cursor.execute(query1)
    print("1. What are the most popular three articles of all time? ")
    for (title, views) in cursor.fetchall():
        print("{} - {} views".format(title, views))

    cursor.execute(query2)
    print("\n2. Who are the most popular authors of all time? ")
    for (authors, totalsbyauthor) in cursor.fetchall():
        print("{} - {} views".format(authors, totalsbyauthor))

    cursor.execute(query3)
    print("\n3. On which days did more than 1% of requests lead to errors? ")
    for (date, percent) in cursor.fetchall():
        print("{} - {}% errors".format(date, percent))

    # closing cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
