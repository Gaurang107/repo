import cv2
import pytesseract
from PIL import Image

# If you're on Windows, specify the tesseract.exe path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
image_path = "text_image.png"   # change to your image file
img = cv2.imread(image_path)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to make text clearer
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Optionally display the image
cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Extract text using pytesseract
extracted_text = pytesseract.image_to_string(thresh)

print("🔠 Recognized Text:")
print(extracted_text)


#pip install pytesseract opencv-python pillow

#sudo apt install tesseract-ocr 
