from pypdf import PdfReader,PdfWriter
import sys
def remove_link(page):
    for annot in page["/Annots"]:
        obj = annot.get_object()
        if obj["/Subtype"] == "/Link" and obj['/Private'] == "/UPDF":
            page["/Annots"].remove(annot)

def remove_updf(page):
    if page["/Resources"]['/XObject'].get('/UPDFX1'):
        del page["/Resources"]['/XObject']['/UPDFX1']

file = sys.argv[1]
reader = PdfReader(file)
writer = PdfWriter()
for page in reader.pages:
    remove_link(page)
    remove_updf(page)
    writer.add_page(page)

with open(file,"wb") as f:
    writer.write(f)
