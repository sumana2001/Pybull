import PyPDF2

#open file in read binary mode
pdfFileObj = open('filename.pdf', 'rb')

#creating a object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#To get the page object
pageObj = pdfReader.getPage(0) #Module uses zero based index

#Extracts the text from specified page
pageObj.extractText()
