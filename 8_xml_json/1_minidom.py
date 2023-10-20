from xml.dom.minidom import parse, Document

document: Document = parse("slideshow.xml")

print(document.childNodes)
print(document.childNodes[0].toxml())
slide_elements = document.firstChild.getElementsByTagName("slide")
print(slide_elements[0].getAttribute("colour"))
print(document.firstChild.childNodes)
for slide_element in slide_elements:
    print(slide_element.toxml())
    print(slide_element.getElementsByTagName("title")[0].toxml())
    print(slide_element.getElementsByTagName("title")[0].firstChild.data)
