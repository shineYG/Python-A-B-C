import PyPDF2

with open('encryptMark.pdf', 'rb') as encryptFile:
    encryptReader = PyPDF2.PdfFileReader(encryptFile)
    if encryptReader.isEncrypted:
        if encryptReader.decrypt('python'):
            print(encryptReader.getPage(0).extractText())
        else:
            print('Wrong password! ')
    else:
       print(encryptReader.getPage(0).extractText()) 