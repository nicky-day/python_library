import sqlite3
from textwrap import wrap
import time

conn = sqlite3.connect("blog.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE blog (id integer PRIMARY KEY, subject text, content text, date text)"""
)
c.execute(
    "INSERT INTO blog VALUES(1, "첫 번째 블로그", "첫 번째 블로그입니다.", "20190827")"
)
c.execute(
    "INSERT INTO blog VALUES(2, "두 번째 블로그", "두 번째 블로그입니다.", "20190827")"
)

_id = 3
subject = "세 번째 블로그"
content = "세 번째 블로그입니다."
date = "20190827"
c.execute(
    "INSERT INTO blog VALUES (%d, '%s', '%s', '%s')" %(_id, subject, content, date)
)


_id = 4
subject = "네 번째 블로그"
content = "네 번째 블로그입니다."
date = "20190827"
c.execute(
    "INSERT INTO blog VALUES (?, ?, ?, ?)", (_id, subject, content, date)
)

c.execute(
    "INSERT INTO blog VALUES (:id, :subject, :content, :date)", {"id":5, "subject":"다섯 번째 블로그", "content":"다섯 번째 블로그입니다.", "date":"20190827"}
)

c.execute("SELECT * FROM blog")
all = c.fetchall()
print(all)

c.execute("SELECT * FROM blog")
one = c.fetchone()
print(one)

c.execute("UPDATE blog SET subject='최초의 블로그' WHERE id=1")

c.execute("SELECT * FROM blog")
one = c.fetchone()
print(one)

c.execute("DELETE FROM blog WHERE id = 5")

conn.commit()

conn.rollback()

conn.close()

'''
def get_blog_list():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("SELECT * FROM blog")
    result = c.fetchall()
    conn.close()
    return result
'''

def get_blog_list():
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT FROM blog")
    result = c.fetchall()
    conn.close()
    return result


for blog in get_blog_list():
    print(blog)
    print(blog["subject"])


def add_blog(subject, content):
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    today = time.strftime("%Y%m%d")
    c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)", (subject, content, today))
    conn.commit()
    conn.close()


def read_blog(_id):
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM blog WHERE id = ?", (_id,))
    result = c.fetchone()
    conn.close()
    return result


def modify_blog(_id, subject, content):
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE blog SET subject=?, content=?, where id = ?", (subject, content, _id))
    conn.commit()
    conn.close()


def remove_blog(_id):
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("DELETE FROM blog where id = ?", (_id))
    conn.commit()
    conn.close()


def with_cursor(original_func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("blog.db")
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rv = original_func(c, *args, **kwargs)
        conn.commit()
        conn.close()
        return rv
    return wrapper

@with_cursor
def get_blog_list(c):
    c.execute("SELECT FROM blog")
    return c.fetchall()

@with_cursor
def add_blog(c, subject, content):
    c.execute("INSERT INTO blob (subject, content, date) VALUES (?, ?, ?)",
        (subject, content, time.strftime("%Y%m%d"))
    )

@with_cursor
def read_blog(c, _id):
    c.execute("SELECT * FROM blog WHERE id = ?", (_id,))
    return c.fetchone()

@with_cursor
def modify_blog(c, _id, subject, content):
    c.execute("UPDATE blog SET subject=?, content=?, WHERE id=?", (subject, content, _id))

@with_cursor
def remove_blog(c, _id):
    c.execute("DELETE FROM blog WHERE id=?", (_id,))
