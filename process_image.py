# process_image.py
import pytesseract
from PIL import Image
from transformers import pipeline

# Function to extract text from an image
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to summarize the extracted text
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Testing with a sample image
if __name__ == "__main__":
    # Replace 'sample_image.jpg' with the path to your image
    image_path = 'sample_image.jpg'
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:", extracted_text)

    summary = summarize_text(extracted_text)
    print("Summary:", summary)
