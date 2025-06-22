import sqlite3
from typing import Any, Optional

class Database:
    def __init__(self, db: str):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            job TEXT NOT NULL,
            geschlecht TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            telefon TEXT NOT NULL,
            adresse TEXT NOT NULL
        )"""
        self.cur.execute(sql)
        self.con.commit()

    def insert_employee(self, name: str, job: str, geschlecht: str, age: int, email: str, telefon: str, adresse: str):
        sql = """INSERT INTO employees (name, job, geschlecht, age, email, telefon, adresse)
                 VALUES (?, ?, ?, ?, ?, ?, ?)"""
        self.cur.execute(sql, (name, job, geschlecht, age, email, telefon, adresse))
        self.con.commit()

    def update_employee(self, emp_id: int, name: str, job: str, geschlecht: str, age: int, email: str, telefon: str, adresse: str):
        sql = """UPDATE employees SET name=?, job=?, geschlecht=?, age=?, email=?, telefon=?, adresse=?
                 WHERE id=?"""
        self.cur.execute(sql, (name, job, geschlecht, age, email, telefon, adresse, emp_id))
        self.con.commit()

    def delete_employee(self, emp_id: int):
        sql = """DELETE FROM employees WHERE id=?"""
        self.cur.execute(sql, (emp_id,))
        self.con.commit()

    def fetch_all_employees(self):
        sql = """SELECT * FROM employees"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def fetch_employee_by_id(self, emp_id: int) -> Optional[Any]:
        sql = """SELECT * FROM employees WHERE id=?"""
        self.cur.execute(sql, (emp_id,))
        return self.cur.fetchone()

    def reset_autoincrement(self):
        """Setzt den AUTOINCREMENT-Zähler der Tabelle 'employees' zurück."""
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name='employees'")
        self.con.commit()

    def delete_all_employees_and_reset_id(self):
        """Löscht alle Datensätze und setzt AUTOINCREMENT zurück auf 1."""
        self.cur.execute("DELETE FROM employees")
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name='employees'")
        self.con.commit()

    def close(self):
        self.con.close()
