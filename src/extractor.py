from pdf2image import convert_from_path
import pytesseract
import cv2
import util
import sys
from pathlib import Path

from parser_patient_details import PatientDetailsParser
from parser_prescription import PrescriptionParser
POPPLER_PATH = r'E:\GOD IS LOVE-Data Analyst Bootcamp\GOD IS LOVE - PYTHON\GosIsLoveMedicalExtract\backend\Release-21.11.0-0\poppler-21.11.0\Library\bin'

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    print('no of pages'+ str(pages))
    document_text = ''
    for page in pages:
        processed_image = util.preprocess_image(page)
        processed_image
        document_text += pytesseract.image_to_string(processed_image, lang='eng')
    print(document_text)
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data
    return document_text
if __name__ == '__main__':
    data = extract(r'{give the path of the prescription document}', 'patient_details')
    print(data)
