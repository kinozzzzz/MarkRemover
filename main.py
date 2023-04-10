from pypdf import PdfReader,PdfWriter
import sys
import re

def remove_link(page):
    for annot in page["/Annots"]:
        obj = annot.get_object()
        if obj["/Subtype"] == "/Link" and obj['/Private'] == "/UPDF":
            print('delete link')
            page["/Annots"].remove(annot)

def remove_resources(page):
    resources = page['/Resources']
    
    def remove(k):
        remove_key = []
        for key in resources[k]:
            if re.search("/UPDF",key):
                remove_key.append(key)
                print('delete mark')
        for key in remove_key:
            del resources[k][key]

    remove('/XObject')
    remove('/ExtGState')

file = sys.argv[1]
reader = PdfReader(file)
writer = PdfWriter()
for page in reader.pages:
    remove_link(page)
    remove_resources(page)
    writer.add_page(page)

with open(file,"wb") as f:
    writer.write(f)
