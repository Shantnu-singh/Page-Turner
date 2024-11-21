from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_pdf_text(pdfs):
    text = ''
    for pdf in pdfs:
        pdfPEaderObj = PdfReader(pdf)
        for page in pdfPEaderObj.pages:
            text += page.extract_text()
            
    return text

def get_chunks(text):
    text_spiltter = RecursiveCharacterTextSplitter(chunk_size = 6000 , chunk_overlap = 700)
    chunks = text_spiltter.split_text(text)
    
    return chunks
    
    
