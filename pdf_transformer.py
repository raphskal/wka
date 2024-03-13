import os
import re
from PIL import Image
import pytesseract
import numpy as np
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\ProgramData\Tesseract\tesseract.exe"

def file_finder(files, FORMAT):
	files_to_rename = []
	for f in files:
		if re.search(FORMAT, f):
			files_to_rename.append(f)
	return files_to_rename

def rename_files(files):
	for f in files:
		pil_image_lst = convert_from_path(f, poppler_path=r'C:\ProgramData\poppler\poppler-24.02.0\Library\bin')
		text = pytesseract.image_to_string(pil_image_lst[0])
		new_name = get_name(text)
		print(f'Renaming {f} to {new_name}.pdf')
		os.rename(f, new_name+'.pdf')
	return

def get_name(txt):
	entnahmeschein = txt.partition("Entnahmeschein ")[2][:5]
	auftragsnr = txt.partition("Auftragsnr.: AUF-")[2][:9]
	return f'{entnahmeschein}_AUF-{auftragsnr}'


if __name__ == '__main__':
	os.chdir(r'C:\Users\rapha\Downloads')
	files = os.listdir()
	files_to_rename = file_finder(files, '^[0-9]+.pdf$')
	print(f'Renaming files {files_to_rename}')
	rename_files(files_to_rename)
	print("Done renaming.")

	

