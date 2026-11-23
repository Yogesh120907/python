class StudentRegistry:
    def __init__(self):
        self.students = {}

    def insert_student(self, student_id: str, name: str, age: int, grade: str) -> bool:
        if student_id in self.students:
            return False
        self.students[student_id] = {"name": name, "age": age, "grade": grade}
        return True

    def delete_student(self, student_id: str) -> bool:
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False

    def search_student(self, student_id: str) -> dict | None:
        return self.students.get(student_id)

if __name__ == "__main__":
    registry = StudentRegistry()
    registry.insert_student("S101", "Alice", 20, "A")
    registry.insert_student("S102", "Bob", 21, "B")
    print("Search S101:", registry.search_student("S101"))
    registry.delete_student("S102")
    print("Search S102 after deletion:", registry.search_student("S102"))
