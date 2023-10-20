import xml.etree.ElementTree as ET

document = ET.parse("slideshow.xml")
print(document.find("slide").attrib["colour"])
print(document.findall("slide")[0].attrib["colour"])
print(document.findall("slide")[0])
print(document.findall("slide")[0].find("title").text)
print([x.text for x in document.findall("title")]) # findall(.//title) zwróci listę obiektów Element o tagu title bezpośrednio wewnątrz aktualnego tagu
print([x.text for x in document.findall(".//title")])  # findall(.//title) zwróci listę obiektów Element o tagu title na dowolnym poziomie zagnieżdżenia
print([x.find("title").text for x in document.findall("slide")])

