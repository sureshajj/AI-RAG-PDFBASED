import os
from pypdf import PdfReader,PdfWriter

def read_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() for page in reader.pages]
    return pages


def extract_page(input_pdf, output_pdf, page_number):
    """
    Extracts a specific page from a PDF.
    page_number: 0-indexed (e.g., page 1 is index 0)
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Get the specific page
    page = reader.pages[page_number]
    writer.add_page(page)
    
    # Write the new PDF
    with open(output_pdf, "wb") as output_stream:
        writer.write(output_stream)
    print(f"Page {page_number + 1} extracted to {output_pdf}")

# Usage: Extract page 2 (index 1)
