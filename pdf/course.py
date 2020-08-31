import PyPDF2

filenames = ['howto-descriptor.pdf', 'howto-argparse.pdf', 'howto-curses.pdf']

merger = PyPDF2.PdfFileMerger()
for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))
merger.write('final.pdf')
