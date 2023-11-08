import PyPDF2 
file_name = open("POSCO Sustainability Report 2022.pdf",'rb')
pdfReader = PyPDF2.PdfReader(file_name)
pdfReader.pages[0]
pdfReader.pages[0].extract_text()
