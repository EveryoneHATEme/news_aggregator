import sqlite3
import csv

connection = sqlite3.connect("app.db")


def create_table():
    connection.execute(
        """
    CREATE TABLE IF NOT EXISTS duplicates(
        id INT PRIMARY KEY ON CONFLICT IGNORE,
        message TEXT,
        label INT
    );
    """
    )


def insert_duplicates(values: list[tuple[int, str, int]]):
    connection.executemany(
        """
    INSERT INTO duplicates(id, message, label) VALUES (?, ?, ?)
    """,
        values,
    )


def get_min_label() -> int:
    result = connection.execute("SELECT min(label) FROM duplicates").fetchone()[0]
    return result or 0


def to_csv(filename: str):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(
            connection.execute("SELECT id, message, label FROM duplicates").fetchall()
        )
