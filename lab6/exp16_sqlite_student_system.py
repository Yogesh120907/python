import sqlite3

def init_database(db_name: str = "student.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_student(roll_no: int, name: str, department: str, cgpa: float, db_name: str = "student.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll_no, name, department, cgpa))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def fetch_all_students(db_name: str = "student.db") -> list[tuple]:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    conn.close()
    return records

if __name__ == "__main__":
    init_database()
    insert_student(101, "Alice", "CS", 8.9)
    insert_student(102, "Bob", "ECE", 7.8)
    students = fetch_all_students()
    for s in students:
        print(f"Roll: {s[0]} | Name: {s[1]} | Dept: {s[2]} | CGPA: {s[3]}")
