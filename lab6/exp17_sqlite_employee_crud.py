import sqlite3

class EmployeeCRUD:
    def __init__(self, db_name: str = ":memory:"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                designation TEXT,
                department TEXT,
                salary REAL
            )
        """)
        self.conn.commit()

    def create(self, emp_id: int, name: str, designation: str, department: str, salary: float):
        self.cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", 
                           (emp_id, name, designation, department, salary))
        self.conn.commit()

    def read(self, emp_id: int = None):
        if emp_id:
            self.cursor.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
            return self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM employee")
        return self.cursor.fetchall()

    def update_salary(self, emp_id: int, new_salary: float):
        self.cursor.execute("UPDATE employee SET salary = ? WHERE emp_id = ?", (new_salary, emp_id))
        self.conn.commit()

    def delete(self, emp_id: int):
        self.cursor.execute("DELETE FROM employee WHERE emp_id = ?", (emp_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    app = EmployeeCRUD()
    app.create(1, "John Doe", "Engineer", "IT", 75000.0)
    app.create(2, "Jane Smith", "Manager", "HR", 85000.0)
    print("Initial Employees:", app.read())
    app.update_salary(1, 80000.0)
    print("Updated Employee 1:", app.read(1))
    app.delete(2)
    print("Remaining Employees:", app.read())
    app.close()
