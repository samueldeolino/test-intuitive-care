from typing import List
import tabula
import pandas as df
import os
import zipfile as zip
from pathlib import Path
import shutil

DIR = Path(__file__).parent.parent
FOLDER_PATH = DIR /'web-scraping'/'scripts'/'Attachments_ANS.zip'
PDF_NAME = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

def unzipFolder(zipPath: str, pdfName: str):

    if not zipPath.exists():
        raise FileNotFoundError(f"Zip file not found: {zipPath}")
    with zip.ZipFile(FOLDER_PATH, 'r') as file:
        if pdfName not in file.namelist():
            raise ValueError('File not found in zip')
        file.extract(pdfName, '.')

def readPdf():
    try:
        dfs = tabula.read_pdf(PDF_NAME, pages='all', multiple_tables=True, lattice=True)
        return dfs
    except Exception as e:
        raise RuntimeError('Failure to reader PDF: {e}')
