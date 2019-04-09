#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def most_popular_posts():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select title, views from articles
        join (select path, count (*) as views from log where status = '200 OK'
        group by path) as pv on pv.path = concat('/article/', articles.slug)
        order by views desc offset 0 limit 3;
        """)
    posts = c.fetchall()
    db.close()
    print("The most popular three articles of all time are:")
    for row in posts:
        print(row[0], "-", row[1], "views")
    print("\n")


most_popular_posts()


def most_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select name, sum(views) as total_views from articles,
        authors, articles_pv where articles_pv.title = articles.title
        and articles.author = authors.id group by name order
        by total_views desc;""")
    authors = c.fetchall()
    db.close()
    print("The most popular article authors of all time are:")
    for row in authors:
        print(row[0], "-", row[1], "views")
    print("\n")


most_popular_authors()


def many_errors_days():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select errors.date, round(100.0 * errors / access, 1)
        as error_rate from errors, total_access
        where errors.date = total_access.date
        and 100.0 * errors / access >= 1.0;""")
    days = c.fetchall()
    db.close()
    print("Days on which more than 1% of requests led to errors are:")
    for row in days:
        print(row[0], "-", row[1], "% errors")
    print("\n")


many_errors_days()
