# OCR PDF to Text Extraction

This project uses Tesseract OCR to extract text from PDF files. The code processes PDF files by converting each page into an image, applying various image processing techniques to enhance the text, and then using OCR to extract the text. The extracted text is saved to corresponding `.txt` files.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [License](#license)

## Features
- Convert PDF pages to images.
- Apply image processing techniques like grayscale conversion, blurring, and thresholding.
- Use contours to detect text regions.
- Extract text from images using Tesseract OCR.
- Save the extracted text to `.txt` files.

## Installation

To run this project, you'll need to set up the necessary Python environment and dependencies. Follow the steps below:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/huseyinbattal3469/pdf-to-png-to-text.git
    cd pdf-to-png-to-text
    ```

2. **Install the required packages**:
    You can install the required Python packages inside:

    ```bash
    packages.txt
    ```

3. **Install Tesseract**:
   Ensure that Tesseract OCR is installed on your machine. You can download it from [Tesseract's official GitHub page](https://github.com/tesseract-ocr/tesseract) and follow the installation instructions.

## Usage

1. **Place your PDF files**:
   Put the PDF files you want to process inside the `pdfs` folder.

2. **Run the script**:
   Execute the script to process the PDFs and extract the text:

   ```bash
   python main.py
   ```

   The script will perform the following steps:
   - Convert each page of the PDFs into images.
   - Process the images to enhance text visibility.
   - Extract the text using Tesseract OCR.
   - Save the extracted text to `.txt` files.

3. **View the results**:
   The extracted text will be saved in the root directory of the project as `pdf_name.txt` (where `pdf_name` is the original name of the PDF without the extension).

## Files

- **Gazete1.txt, Gazete2.txt, Gazete3.txt, Gazete4.txt**: Sample text files generated from PDF files.
- **packages.txt**: Contains a list of required Python packages.
- **images folder**: Stores the processed images, including grayscale, blurred, thresholded, dilated, and cropped images.
- **pdfs folder**: Stores the input PDF files.

## License

This project is licensed under the MIT License.
