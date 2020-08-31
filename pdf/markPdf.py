import PyPDF2

with open('howto-curses.pdf', 'rb') as pdfFile:
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    firstPage = pdfReader.getPage(0)

    with open('mark.pdf', 'rb') as markFile:
        markReader = PyPDF2.PdfFileReader(markFile)
        firstPage.mergePage(markReader.getPage(0))

        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(firstPage)

        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        with open('finishMark.pdf', 'wb') as resultPdfFile:
            pdfWriter.write(resultPdfFile)


