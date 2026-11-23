"""
Experiment 22: Parse and display data from an XML document.
"""
import os
import xml.etree.ElementTree as ET

XML_FILE = "courses.xml"

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<university name="Assam Central Institute">
    <course code="CS101" credits="4">
        <title>Python Programming</title>
        <instructor>Dr. R. Sharma</instructor>
        <department>Computer Science</department>
    </course>
    <course code="CS204" credits="3">
        <title>Database Management Systems</title>
        <instructor>Prof. A. Das</instructor>
        <department>Computer Science</department>
    </course>
    <course code="MA102" credits="4">
        <title>Linear Algebra and Calculus</title>
        <instructor>Dr. P. Bora</instructor>
        <department>Mathematics</department>
    </course>
</university>
"""


def parse_and_display():
    if not os.path.exists(XML_FILE):
        with open(XML_FILE, "w", encoding="utf-8") as f:
            f.write(SAMPLE_XML)

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    print(f"University: {root.attrib.get('name')}")
    print("-" * 60)
    for course in root.findall("course"):
        code = course.attrib.get("code")
        credits = course.attrib.get("credits")
        title = course.find("title").text
        instructor = course.find("instructor").text
        dept = course.find("department").text
        print(f"[{code}] {title} ({credits} Credits) | {instructor} - {dept}")


if __name__ == "__main__":
    parse_and_display()
