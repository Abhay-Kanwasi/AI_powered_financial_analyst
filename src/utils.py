"""
Utility functions for the AI-powered financial analyst.
"""
import os
from config import DEFAULT_DATA_DIR

def get_pdf_path():
    """
    Gets the path to the PDF file, either from user input or by finding
    a PDF in the default data directory.
    
    Returns:
        str: Path to the PDF file
    """
    # Check if there's a PDF in the data directory
    pdf_files = [f for f in os.listdir(DEFAULT_DATA_DIR) if f.lower().endswith('.pdf')]
    print(pdf_files)
    if pdf_files:
        # If there's only one PDF, use it automatically
        if len(pdf_files) == 1:
            return os.path.join(DEFAULT_DATA_DIR, pdf_files[0])
        
        # If there are multiple PDFs, let the user choose
        print("Available PDF files:")
        for i, pdf_file in enumerate(pdf_files):
            print(f"{i+1}. {pdf_file}")
        
        selection = int(input("Select a PDF file (number): ")) - 1
        return os.path.join(DEFAULT_DATA_DIR, pdf_files[selection])
    
    # If no PDFs found, ask for a path
    pdf_path = input("Enter the path to your PDF file: ")
    return pdf_path
