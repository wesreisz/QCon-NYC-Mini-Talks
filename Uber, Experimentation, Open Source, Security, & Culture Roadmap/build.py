import os
from PyPDF2 import PdfFileReader, PdfFileMerger

merged_file_name="MergedDeck.pdf"
files_dir = "./" 
if os.path.exists(merged_file_name):
	os.remove(merged_file_name)
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
merger = PdfFileMerger()
for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(files_dir, merged_file_name))
