import PyPDF2 as pdf

pd_merge=pdf.PdfWriter()

pd_merge.append("pyPDF2/1.pdf")
pd_merge.append("pyPDF2/2.pdf")
pd_merge.append("pyPDF2/3.pdf")
pd_merge.append("pyPDF2/4.pdf")

with open("pyPDF2/merged.pdf","wb") as merged:
  pd_merge.write(merged)