from textwrap import indent
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
note.attrib["date"] = "20120104"

to = Element("to")
to.text = "Tove"
note.append("to")

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

# XML을 보기 좋게 만들어 저장
from xml.dom import minidom
import xml.etree.ElementTree as ET

xmlstr = minidom.parseString(ET.tostring(note)).toprettyxml(indent="    ")
print(xmlstr)

# XML을 파일로 저장
with open("note.xml", "w") as f:
    f.write(xmlstr)
