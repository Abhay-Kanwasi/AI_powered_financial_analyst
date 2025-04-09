"""
Functions for extracting text from PDF files.
"""
import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Verify file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        # Open the PDF file
        doc = fitz.open(pdf_path)

        if doc.page_count == 0:
            return "The PDF appears to be empty (zero pages)."

        # Extract text
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            page_text = page.get_text("text")
            text += f"\n--- Page {page_num+1} ---\n{page_text}"

        # Check if extraction was successful
        if not text.strip():
            return "Extraction failed: No text found in document. The PDF may be scanned or image-based."

        return text

    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return f"Failed to extract text: {str(e)}"