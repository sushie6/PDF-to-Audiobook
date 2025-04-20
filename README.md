# PDF-to-Audiobook
This Python script provides a command-line tool to convert PDF files into audiobooks. It utilizes the 'pypdf' library to extract text content from the PDF and the 'pyttsx3' library for text-to-speech synthesis.

# Key Features:
- Takes the full path to a PDF file as input.
- Prompts the user for the desired name of the output audio file.
- Saves the generated audio file (in MP3 format) within a 'sample' folder in the same directory as the script.
- Automatically creates the 'sample' output folder if it doesn't exist.
- Includes error handling for file not found scenarios and potential issues during PDF reading or text-to-speech conversion.
- Provides informative messages to the user about the process and the location of the saved audio file.

# How to Use:
1. Save the script as a Python file (e.g., `pdf_audio_converter.py`).
2. Ensure you have the 'pypdf' and 'pyttsx3' libraries installed. You can install them using pip:
   ```bash
   pip install pypdf pyttsx3
