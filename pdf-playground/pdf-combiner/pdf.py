import PyPDF2
import sys

# ! It's a standard to read PDF in binary format, that is why 'RB'.

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super_merge.pdf')

pdf_combiner(inputs)