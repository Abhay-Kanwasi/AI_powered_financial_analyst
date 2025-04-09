#!/bin/bash
# Script to set up OCR support for PDF extraction

echo "Setting up OCR support for PDF extraction..."

# Install Python packages
pip install pytesseract pillow

# Install Tesseract OCR
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install tesseract
else
    # Windows or other
    echo "Please install Tesseract OCR manually:"
    echo "Windows: https://github.com/UB-Mannheim/tesseract/wiki"
    echo "Other: https://tesseract-ocr.github.io/tessdoc/Installation.html"
fi

echo "OCR setup complete!"
echo "You can now extract text from scanned PDFs."