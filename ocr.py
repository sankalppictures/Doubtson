# ocr.py
import pytesseract
from PIL import Image
import os

# Tesseract executable path (change this if Tesseract is not in your PATH)
# For Windows, it might look like: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# For Linux/macOS, if it's in your PATH, you might not need this line.
# If you get an error like "tesseract is not installed or not in your PATH", uncomment and adjust this line.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    """
    Performs OCR on the given image path using Tesseract.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image. Returns an empty string if OCR fails.
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return ""

    try:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Perform OCR
        extracted_text = pytesseract.image_to_string(img, lang='eng+hin') # 'eng' for English, 'hin' for Hindi

        # Clean up the text (remove extra whitespace, newlines)
        extracted_text = extracted_text.strip()
        print(f"OCR successful for {image_path}. Extracted text length: {len(extracted_text)}")
        return extracted_text
    except pytesseract.TesseractNotFoundError:
        print("Error: Tesseract is not installed or not in your PATH.")
        print("Please install Tesseract OCR engine and ensure it's accessible in your system's PATH.")
        print("Download from: https://tesseract-ocr.github.io/tessdoc/Downloads.html")
        return ""
    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return ""

if __name__ == '__main__':
    # Example usage (for testing purposes)
    # Create a dummy image file for testing if you don't have one
    # from PIL import Image, ImageDraw, ImageFont
    # try:
    #     font = ImageFont.truetype("arial.ttf", 20) # You might need to specify a font path
    # except IOError:
    #     font = ImageFont.load_default()
    #
    # img_test = Image.new('RGB', (300, 100), color = (255, 255, 255))
    # d = ImageDraw.Draw(img_test)
    # d.text((10,10), "Hello World!", fill=(0,0,0), font=font)
    # d.text((10,40), "नमस्ते दुनिया!", fill=(0,0,0), font=font)
    # test_image_path = "test_image.png"
    # img_test.save(test_image_path)
    # print(f"Created dummy image: {test_image_path}")

    # Replace 'test_image.png' with the actual path to your test image
    test_image_path = "path/to/your/question_image.png" # <--- IMPORTANT: Change this to a real image path for testing

    if os.path.exists(test_image_path):
        text = perform_ocr(test_image_path)
        if text:
            print("\n--- Extracted Text ---")
            print(text)
            print("----------------------")
        else:
            print("\nOCR failed or no text extracted.")
    else:
        print(f"\nTest image not found at '{test_image_path}'. Please create one or update the path.")
        print("To test, you can manually place an image in the 'uploads' folder (e.g., 'uploads/my_question.png')")
        print("and then run 'python ocr.py' after changing 'test_image_path'.")

