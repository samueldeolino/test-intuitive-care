import requests
from bs4 import BeautifulSoup
import os
import re
import shutil

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

FOLDER_NAME = 'PDF_Files'
ZIP_FILENAME = 'Attachments_ANS'

def fetchPdfLinks():
    try:
        response = requests.get(URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        pdf_links = [a['href'] for a in soup.find_all('a', href=re.compile(r'Anexo_.*\.pdf'))]

        if pdf_links:
            return pdf_links
        else:
            f'Not found pdf'

    except Exception as f:
        print(f'Error fetching links: {f}')

def downloadFile(urlPdf):
    try:
        response = requests.get(urlPdf)
        response.raise_for_status()

        fileName = os.path.join(FOLDER_NAME, os.path.basename(urlPdf))

        with open(fileName, 'wb') as f:
                f.write(response.content)

    except Exception as e:
        f'An error occurred: {e}'

def main():
    pdf_links = fetchPdfLinks()
    os.makedirs(FOLDER_NAME, exist_ok=True)

    if pdf_links:
        for link in pdf_links:
            downloadFile(link)

    shutil.make_archive(ZIP_FILENAME, format='zip', root_dir=FOLDER_NAME, base_dir='.')
    shutil.rmtree('./PDF_Files')

if __name__ == "__main__":
    main()