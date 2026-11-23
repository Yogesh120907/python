import sqlite3

def setup_payroll_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE employee (
            emp_id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary REAL
        )
    """)
    sample_data = [
        (1, "Alice", "Engineering", 90000),
        (2, "Bob", "Engineering", 80000),
        (3, "Charlie", "HR", 60000),
        (4, "Diana", "HR", 65000),
        (5, "Evan", "Marketing", 70000)
    ]
    cursor.executemany("INSERT INTO employee VALUES (?, ?, ?, ?)", sample_data)
    conn.commit()

def generate_dept_salary_report(conn, department_name: str) -> dict:
    cursor = conn.cursor()
    query = """
        SELECT 
            COUNT(emp_id),
            SUM(salary),
            AVG(salary),
            MIN(salary),
            MAX(salary)
        FROM employee
        WHERE department = ?
    """
    cursor.execute(query, (department_name,))
    result = cursor.fetchone()
    return {
        "department": department_name,
        "headcount": result[0],
        "total_expenditure": result[1],
        "average_salary": result[2],
        "min_salary": result[3],
        "max_salary": result[4]
    }

if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")
    setup_payroll_db(connection)
    for dept in ["Engineering", "HR", "Marketing"]:
        report = generate_dept_salary_report(connection, dept)
        print(f"--- Salary Report: {report['department']} ---")
        print(f"Headcount: {report['headcount']}")
        print(f"Total Expenditure: ${report['total_expenditure']:.2f}")
        print(f"Average Salary: ${report['average_salary']:.2f}\n")
    connection.close()
