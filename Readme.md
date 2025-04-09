# AI-Powered Financial Analyst

This project uses LangChain with Groq's LLM to analyze financial reports from PDF files. It has been optimized for simplicity and efficiency.

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Place your PDF file in the `data/` directory and run:
```
python main.py
```

## Features

- Efficient PDF text extraction
- Financial data analysis using Groq's LLama-3 model
- Conversational AI agent with memory
- Streamlined codebase for better performance

## Optional OCR Support

If you need to extract text from scanned or image-based PDFs, you can enable OCR support:

1. Uncomment the OCR dependencies in `requirements.txt`
2. Install the dependencies: `pip install -r requirements.txt`
3. Install Tesseract OCR on your system (see setup_ocr.sh for instructions)
