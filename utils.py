# correct code for this file


import cv2
import pytesseract as pt
import re
# import numpy as np

# Define valid state codes and license plate regex
VALID_STATE_CODES = {
    'AN', 'AP', 'AR', 'AS', 'BR', 'CG', 'DL', 'DN', 'GA', 'GJ',
    'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'LA', 'MH', 'ML', 'MN',
    'MP', 'MZ', 'NL', 'OD', 'PB', 'RJ', 'PY', 'SK', 'WB', 'UP',
    'TN', 'TR', 'TS', 'UK'
}
# LICENSE_PLATE_REGEX = r"^([A-Z]{2})(0[1-9]|[1-9][0-9]{1,2})([A-Z]{1,3})([0-9]{4})$"
LICENSE_PLATE_REGEX = r"^([A-Z]{2})(\d{1,2})([A-Z]{1,3})(\d{4})$"
# numbers = {''} 
numbers = set()
det_text = set()
val_text = set()

# numbers = {"AN 74 VJ 7317", 'AN01H0908' , "AN01H1689"}
def crop(frame, box):
    box = box[0]
    co_ordinate = []
    for i in box:
        co_ordinate.append(round(i))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    numberplate = image[co_ordinate[1]:co_ordinate[3], co_ordinate[0]:co_ordinate[2]]
    ocr(numberplate)


# def ocr(image):

#     number=(pt.image_to_string(image))
#     numbers.add(number)

def ocr(image):
    try:
        # Perform OCR on the image
        detected_text = pt.image_to_string(image,
                                           config='--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789').strip()
        detected_text = detected_text.replace(" ", "")



        # Validate the detected text using regex
        if re.match(LICENSE_PLATE_REGEX, detected_text):
            state_code = detected_text[:2]
            det_text.add(detected_text)# Extract the state code (first 2 characters)

            if state_code in VALID_STATE_CODES:  # Check if the state code is valid
                numbers.add(detected_text)  # Add the valid license plate to the set
                val_text.add("Valid")
                print(f"Valid License Plate Detected: {detected_text}")
            else:
                # numbers.add(detected_text)
                print(f"Invalid State Code: {detected_text}")
        else:
            det_text.add(detected_text)
            print(f"Invalid License Plate Format: {detected_text}")

    except Exception as e:
        print(f"OCR Error: {e}")





