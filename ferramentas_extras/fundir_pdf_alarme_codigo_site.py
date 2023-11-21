from PyPDF2 import PdfFileReader, PdfFileMerger #pip intall

arq1 = PdfFileReader('Arquivo1.pdf')
arq1 = PdfFileReader('Arquivo1.pdf')

mesclando = PdfFileMerger()
print(mesclando)
mesclando.append(arq1)
mesclando.append(arq2)

mesclando.write('Arquivo3.pdf')