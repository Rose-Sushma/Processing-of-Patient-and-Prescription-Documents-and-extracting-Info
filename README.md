# Processing-of-Patient-and-Prescription-Documents-and-extracting-Info
Prerequisites:

Create a conda environment . conda create --name
Activate the created environment. conda activate
Run the below commands in your created environment
pdf2image==1.10.0 pytesseract==0.3.0 opencv_python==4.3.0.38--4.1.2.30 numpy==1.19.4 pandas==0.25.3 Pillow==7.0.0 fastapi[all] pytest==6.2.2

Install Postman
Problem statement:

There are prescription and patient detail documents. The images or document are not so clear which has images within document hence the text are not clear. Hence image processing is done using tesseract OCR and extracting the document. code attached.

Testing: Pytest is used. Also postman is used for testing.
