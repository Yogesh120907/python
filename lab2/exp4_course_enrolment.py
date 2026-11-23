def analyze_enrolments(course_a_students: set, course_b_students: set) -> dict:
    return {
        "both_courses": course_a_students.intersection(course_b_students),
        "all_students": course_a_students.union(course_b_students),
        "only_course_a": course_a_students.difference(course_b_students),
        "only_course_b": course_b_students.difference(course_a_students),
        "exactly_one_course": course_a_students.symmetric_difference(course_b_students)
    }

if __name__ == "__main__":
    cs101_students = {("S1", "Alice"), ("S2", "Bob"), ("S3", "Charlie")}
    math201_students = {("S2", "Bob"), ("S4", "David")}
    analysis = analyze_enrolments(cs101_students, math201_students)
    for key, val in analysis.items():
        print(f"{key.replace('_', ' ').title()}: {val}")
