import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_pdfs(url, folder="pdf_files"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    pdf_links = set()
    for link in soup.find_all("a", href=True):
        href = link['href']
        if href.lower().endswith(".pdf"):
            full_url = urljoin(url, href)
            pdf_links.add(full_url)

    print(f"Found {len(pdf_links)} PDF files.")

    for pdf_url in pdf_links:
        filename = os.path.join(folder, os.path.basename(urlparse(pdf_url).path))
        print(f"Downloading {pdf_url}...")
        pdf_response = requests.get(pdf_url)
        with open(filename, "wb") as f:
            f.write(pdf_response.content)
    print("Done.")

if __name__ == "__main__":
    site_url = ""  # add url link here
    download_pdfs(site_url)
