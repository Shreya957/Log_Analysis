#!/usr/bin/env python3

import psycopg2
from datetime import datetime

DBNAME = "news"


def main():
    print "\n"
    print "\n"
    get_q1()
    print "\n"
    get_q2()
    print "\n"
    get_q3()


def get_q1():
    print """The most popular three articles of all time are """
    print "..."
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select title, count(title) as title_count
              from log_analysis
              where status like '%200%' and title != ''
              group by title order by title_count DESC limit 3""")
    posts = c.fetchall()
    i = 0
    for i in range(len(posts)):
        print("\"" + str(posts[i][0]) + "\" - " + str(posts[i][1]) + " views")
    db.close()


def get_q2():
    print """The most popular article authors of all time are """
    print "..."
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select A.name, count(L.title) as title_count
              from log_analysis as L, authors as A
              where L.status like '%200%' and L.auth_id=A.id
              group by L.title, A.name order by title_count desc""")
    posts = c.fetchall()
    i = 0
    for i in range(len(posts)):
        print(str(posts[i][0]) + " " + "-" + " " + str(posts[i][1]) + " views")
    db.close()


def get_q3():
    print"""Days on which more than 1% of requests lead to errors are"""
    print "..."
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql = """select D,per_cen from
            (select dc.fail_count/ab.total*100 per_cen,ab.date_id as D
            from (select count(status) fail_count,date(time) as date_id1
            from log where status='404 NOT FOUND'
            GROUP BY status,date_id1 ORDER BY date_id1) as dc,
            (select SUM (FAIL_COUNT) TOTAL,date_id
            from (select count(status) as fail_count,
            status, date(time) as date_id
            from log  where status in ('404 NOT FOUND','200 OK')
            GROUP BY status,date_id ORDER BY date_id)
            as a group by date_id order by date_id) as ab
            WHERE  ab.date_id = dc.date_id1) as xyz where per_cen > 1;"""

    c.execute(sql)
    posts = c.fetchall()
    i = 0
    for i in range(len(posts)):
        datetimeobject = datetime.strptime(str(posts[i][0]), '%Y-%m-%d')
        new_date = datetimeobject.strftime('%b %d, %Y')
        print(new_date + " - " + "%.2f" % posts[i][1] + "% errors")
    db.close()


if __name__ == '__main__':
    main()
