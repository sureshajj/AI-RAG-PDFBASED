from pdfreader import read_pdf
from pdfreader import extract_page
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_in_pinecone
from typing import List

pdf_path = "C:/VSC/pdfs/MDMDoc.pdf"
pdf_path2 = "C:/VSC/pdfs/MDMDoc2.pdf"
#pdf_path="./resources/HRPolicy.pdf"
def run():
    # Read HR Policy PDF and extract text


    extract_page(pdf_path, pdf_path2, 2)


   
    pages = read_pdf(pdf_path2)
    print("Extractex len(pages): ", len(pages))
    print("first page contents")
    print(pages[0] if pages else "No pages extracted.")

    # Chunk the extracted text into manageable pieces

    chunks = chunk_pages(pages, chunk_size=900, chunk_overlap=150)

    embedded_chunks = embed_chunks(chunks)
    
    store_in_pinecone(chunks, embedded_chunks, namespace="")
   
    
if __name__ == "__main__":
    run()