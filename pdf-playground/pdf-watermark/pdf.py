import PyPDF2
import sys

input_pdf = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermk = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(input_pdf.getNumPages()):
    pdf_page = input_pdf.getPage(i)
    pdf_page.mergePage(watermk.getPage(0))
    output.addPage(pdf_page)

with open(f'watermk--{sys.argv[1]}', 'wb') as file:
    output.write(file)
