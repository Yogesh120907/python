import os

def assign_grade(average: float) -> str:
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    return 'F'

def process_student_records(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write("Name,Total,Average,Grade\n")
        for line in infile:
            parts = line.strip().split(',')
            if not parts or len(parts) < 2:
                continue
            name = parts[0].strip()
            marks = [float(m.strip()) for m in parts[1:]]
            total = sum(marks)
            avg = total / len(marks)
            grade = assign_grade(avg)
            outfile.write(f"{name},{total:.2f},{avg:.2f},{grade}\n")

if __name__ == "__main__":
    input_filename = "student_marks.txt"
    output_filename = "student_grades.txt"
    with open(input_filename, 'w') as f:
        f.write("Alice,85,90,88\nBob,70,65,72\nCharlie,95,92,98\n")
    process_student_records(input_filename, output_filename)
    with open(output_filename, 'r') as f:
        print(f.read())
    if os.path.exists(input_filename):
        os.remove(input_filename)
    if os.path.exists(output_filename):
        os.remove(output_filename)
