import pypdf
import pyttsx3
import os

def pdf_to_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except FileNotFoundError:
        print(f"Error: File not found at {pdf_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return None
    return text

def text_to_speech(text, audio_path):
    if text:
        engine = pyttsx3.init()
        try:
            engine.save_to_file(text, audio_path)
            engine.runAndWait()
            print(f"Audio saved to {audio_path}")
        except Exception as e:
            print(f"An error occurred during text-to-speech conversion: {e}")
    else:
        print("No text to convert to speech.")

def pdf_to_audio(pdf_path, audio_path):
    text = pdf_to_text(pdf_path)
    if text is not None:
        text_to_speech(text, audio_path)

if __name__ == "__main__":
    pdf_path = input("Enter the full path to the PDF file: ")
    output_name = input("Enter the desired name for the audio file (without extension): ")
    output_folder = "sample"
    audio_path = os.path.join(output_folder, f"{output_name}.mp3")

    os.makedirs(output_folder, exist_ok=True)

    pdf_to_audio(pdf_path, audio_path)
    print(f"Your audio file has been saved to the '{output_folder}' folder.")