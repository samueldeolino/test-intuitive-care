import tabula
import pandas as df
import os
import zipfile as zip
from pathlib import Path

DIR = Path(__file__).parent.parent
FOLDER_PATH = DIR /'web-scraping'/'scripts'/'Attachments_ANS.zip'

print(FOLDER_PATH)
OD = 'Seg. Odontológica'.upper()
AMB = 'Seg. Ambulatorial'.upper()
columns_map = {'OD': OD, 'AMB': AMB}

def unzipFolder(zipPath: str, pdfName: str):

    if not zipPath.exists():
        raise FileNotFoundError(f"Zip file not found: {zipPath}")
    with zip.ZipFile(FOLDER_PATH, 'r') as file:
        if pdfName not in file.namelist():
            raise ValueError('File not found in zip')
        file.extract(pdfName, '.')

unzipFolder(FOLDER_PATH, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')