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

def convertToCsv(dfs: List[df.DataFrame]):

    OD = 'Seg. Odontológica'.upper()
    AMB = 'Seg. Ambulatorial'.upper()
    columns_map = {'OD': OD, 'AMB': AMB}

    dfs_concatenado = df.concat(dfs, ignore_index=True)
    dfs_concatenado.rename(columns=columns_map, inplace=True)
    dfs_concatenado.drop(columns=['Unnamed: 0'], inplace=True)
    dfs_concatenado.to_csv('output.csv', index=False)

def main():
    unzipFolder(FOLDER_PATH, PDF_NAME)
    a = readPdf()
    convertToCsv(a)
    shutil.make_archive(format='zip', root_dir='.', base_dir='output.csv', base_name='Teste_Samuel_Deolino')
    
    files = [PDF_NAME, 'output.csv']
    for remove in files:
        os.remove(remove)

if __name__ == "__main__":
    main()