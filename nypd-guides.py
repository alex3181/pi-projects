import fitz  # imports the pymupdf library
import os


def extract_text_from_pdf(pdf_file_path):
    pdf_text = ""
    with fitz.open(pdf_file_path) as doc:  # open a document
        for page in doc:  # iterate the document pages
            pdf_text = pdf_text + page.get_text()  # get plain text encoded as UTF-8

    pdf_text = pdf_text.replace("NEW  YORK  CITY  POLICE  DEPARTMENT", "")
    pdf_text = pdf_text.replace("\t", "")
    pdf_text = pdf_text.replace("\r", "")
    pdf_text = pdf_text.replace("\r\n", "")
    pdf_text = pdf_text.strip()
    return pdf_text


def list_files(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Current directory: {root}")
        print("Files:")
        for file in files:
            print(os.path.join(root, file))


if __name__ == "__main__":
    manuals_directory = "./manuals/"
    pdf_file_path = "./manuals/202-02.pdf"

    # print(extract_text_from_pdf(pdf_file_path))

list_files(manuals_directory)
