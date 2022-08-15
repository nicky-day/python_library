from dataclasses import dataclass
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"
note.attrib["data"] = "20120104"
# note = Element("note", date="20120104")

dump(note)
