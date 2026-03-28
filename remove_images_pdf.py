"""
This script removes all images from a PDF using PyMuPDF (fitz).
It opens the input PDF, iterates through pages, finds image xrefs
and deletes them, then saves the result to a new PDF.

Install dependency:
pip install pymupdf
"""

import fitz


def remove_images_from_pdf(input_pdf: str) -> None:
    doc = fitz.open(input_pdf)

    for page in doc:
        image_list = page.get_images()
        for img in image_list:
            xref = img[0]
            page.delete_image(xref)

    doc.save(f'noimages-{input_pdf}', garbage=3, deflate=True)
    doc.close()


if __name__ == "__main__":
    remove_images_from_pdf("file.pdf")
