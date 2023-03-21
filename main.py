import pytesseract as tsr
from PIL import Image
import cv2
import pdf2image as pdfc
import os

"""
Page segmentation modes:

1. Orientation and script detection (OSD) only.

2. Automatic page segmentation with OSD.

3. Automatic page segmentation, but no OSD, or OCR. (not implemented)

4. Fully automatic page segmentation, but no OSD. (Default)

5. Assume a single column of text of variable sizes.

6. Assume a single uniform block of vertically aligned text.

7. Assume a single uniform block of text.

8. Treat the image as a single text line.

9. Treat the image as a single word.

10. Treat the image as a single word in a circle.

11. Treat the image as a single character.

12. Sparse text. Find as much text as possible in no particular order.

13. Sparse text with OSD.

14. Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

OCR Engine modes:

1. Legacy engine only.
2. Neural nets LSTM engine only.
3. Legacy + LSTM engines.
4. Default, based on what is available.
"""
pdfs_path = os.listdir(f"{os.getcwd()}/pdfs")
for pdf in pdfs_path:
    if not pdf.endswith(".pdf"):
        continue
    print(pdf,"dosyası çekiliyor...")
    pages = pdfc.convert_from_path(f"pdfs/{pdf}")
    for page,n in zip(pages,range(0,len(pages))):
        page.save(f"images/out{n}.jpg","JPEG")

        image = cv2.imread(f"images/out{n}.jpg")#
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"images/gray{n}.jpg",gray)

        blur = cv2.GaussianBlur(gray,(7,7),0)
        cv2.imwrite(f"images/blurredgray{n}.jpg",blur)

        thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imwrite(f"images/threshold{n}.jpg",thresh)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(50,13))

        dilate = cv2.dilate(thresh,kernel,iterations=1)
        cv2.imwrite(f"images/dilate{n}.jpg",dilate)

        cnts = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        #print(cnts)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        cnts = sorted(cnts, key=lambda x:cv2.boundingRect(x)[0])

        for contour in cnts:
            x,y,w,h = cv2.boundingRect(contour)
            if h > 200 and w > 20:
                cv2.imwrite(f"images/cropped_image{n}.jpg",image[y:y+h,x:x+w])
                cv2.rectangle(image,(x,y),(x+w,y+h),(36,255,12),2)
        cv2.imwrite(f"images/withboxes{n}.jpg",image) 

        img_strings = tsr.image_to_string(cv2.imread(f"images/cropped_image{n}.jpg"),"tur")
        with open(f"{pdf}.txt","a",encoding="utf-8") as f:
            f.write(img_strings)

