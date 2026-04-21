import sqlite3
from datetime import datetime

# Database file name
DATABASE = "database.db"


# CONNECT TO DATABASE
def connect_db():
    return sqlite3.connect(DATABASE)


# CREATE TABLES
def init_db():

    conn = connect_db()
    cursor = conn.cursor()

    # USERS TABLE

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT DEFAULT 'user',
            created_at TEXT
        )
        """
    )

    # COMPLAINTS TABLE

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            complaint_text TEXT,
            category TEXT,
            sentiment TEXT,
            keywords TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TEXT
        )
        """
    )

    conn.commit()
    conn.close()


# INSERT USER
def insert_user(name, email, password):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (name, email, password, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (name, email, password, datetime.now())
    )

    conn.commit()
    conn.close()


# GET USER BY EMAIL
def get_user(email):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# INSERT COMPLAINT
def insert_complaint(data):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO complaints (
            user_id,
            complaint_text,
            category,
            sentiment,
            keywords,
            priority,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        data
    )

    conn.commit()
    conn.close()


# GET ALL COMPLAINTS
def get_all_complaints():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM complaints"
    )

    data = cursor.fetchall()

    conn.close()

    return data


# OPTIONAL: UPDATE STATUS (useful feature)
def update_status(complaint_id, status):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE complaints
        SET status=?
        WHERE id=?
        """,
        (status, complaint_id)
    )

    conn.commit()
    conn.close()