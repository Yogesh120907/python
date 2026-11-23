"""
Experiment 23: Generate and modify XML documents for student information management.
"""
import xml.etree.ElementTree as ET

XML_FILE = "students_records.xml"


def generate_xml():
    root = ET.Element("students")
    initial_students = [
        {"roll": "2026CS01", "name": "Aarav Sharma", "dept": "CSE", "cgpa": "8.7"},
        {"roll": "2026CS02", "name": "Priya Nair", "dept": "ECE", "cgpa": "9.1"},
        {"roll": "2026CS03", "name": "Rohan Das", "dept": "ME", "cgpa": "7.9"},
    ]
    for s in initial_students:
        student_el = ET.SubElement(root, "student", roll=s["roll"])
        ET.SubElement(student_el, "name").text = s["name"]
        ET.SubElement(student_el, "department").text = s["dept"]
        ET.SubElement(student_el, "cgpa").text = s["cgpa"]

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)
    print(f"Generated '{XML_FILE}'.")


def modify_xml():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    for student in root.findall("student"):
        if student.attrib.get("roll") == "2026CS01":
            student.find("cgpa").text = "9.0"

    new_student = ET.SubElement(root, "student", roll="2026CS04")
    ET.SubElement(new_student, "name").text = "Sneha Roy"
    ET.SubElement(new_student, "department").text = "CSE"
    ET.SubElement(new_student, "cgpa").text = "9.3"

    for student in root.findall("student"):
        if student.attrib.get("roll") == "2026CS03":
            root.remove(student)

    ET.indent(tree, space="  ")
    tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)
    print(f"Modified '{XML_FILE}':")
    with open(XML_FILE, "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    generate_xml()
    modify_xml()
