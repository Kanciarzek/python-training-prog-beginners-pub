from xml.sax import ContentHandler, parse
from xml.sax.xmlreader import AttributesImpl


class CustomContentHandler(ContentHandler):

    def __init__(self):
        super().__init__()
        self.isInSlide: bool = False
        self.isInTitle: bool = False

    def startElement(self, tag_name, attrs: AttributesImpl):
        if tag_name == 'slide':
            self.isInSlide = True
            if "colour" in attrs.keys():
                print(attrs.get("colour"))
        elif tag_name == "title":
            self.isInTitle = True

    def endElement(self, tagName):
        if tagName == 'slide':
            self.isInSlide = False
        elif tagName == "title":
            self.isInTitle = False

    def characters(self, chars):
        if self.isInTitle and self.isInSlide:
            print(chars)


handler = CustomContentHandler()

parse('slideshow.xml', handler)
