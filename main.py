import PyPDF2,sys,os

import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()
path = sys.argv[1]

for file in os.listdir(path):
    # print(file)
    if file.endswith(".pdf"):
        merger.append(path+"/"+file)
    merger.write(path+"/"+"combined.pdf")

